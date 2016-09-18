import itertools

import graphene
from django.db import models
from django.db.models.expressions import F, Value
from django.db.models.functions import Concat
from graphene import relay
from graphene_django import DjangoObjectType

from .models import House, Person, Street


class Relationship(graphene.Enum):
    parent = 'parent'
    grandparent = 'grandparent'
    child = 'child'
    grandchild = 'grandchild'
    spouse = 'spouse'
    sibling = 'sibling'


class StreetNode(DjangoObjectType):
    houses = relay.ConnectionField(lambda: HouseNode)

    class Meta:
        model = Street
        only_fields = ['name']
        interfaces = (relay.Node,)

    def resolve_houses(self, args, context, info):
        return self.house_set.all()


class HouseNode(DjangoObjectType):
    name = graphene.String()
    residents = graphene.ConnectionField(lambda: PersonNode)

    class Meta:
        model = House
        only_fields = ['street', 'number']
        interfaces = (relay.Node,)

    def resolve_name(self, args, context, info):
        return str(self)

    def resolve_residents(self, args, context, info):
        return self.person_set.all()


class PersonNode(DjangoObjectType):
    relationships = graphene.ConnectionField(lambda: PersonNode, relationship=graphene.Argument(Relationship, required=True))

    class Meta:
        model = Person
        only_fields = ['name', 'family', 'residence']
        interfaces = (relay.Node,)

    def resolve_relationships(self, args, context, info):
        if args['relationship'] == 'parent':
            return Person.objects.filter(children=self)
        if args['relationship'] == 'grandparent':
            return Person.objects.filter(children__children=self)
        if args['relationship'] == 'child':
            return Person.objects.filter(parents=self)
        if args['relationship'] == 'spouse':
            if self.spouse:
                return [self.spouse]
        if args['relationship'] == 'grandchild':
            return Person.objects.filter(parents__parents=self)
        if args['relationship'] == 'sibling':
            return Person.objects.filter(parents=self.parents.all()).exclude(pk=self.pk)
        return []


class Anything(graphene.types.union.Union):
    class Meta:
        types = (PersonNode, HouseNode, StreetNode)


class Query(graphene.ObjectType):
    streets = graphene.List(StreetNode)
    search = graphene.Field(graphene.List(Anything), q=graphene.Argument(graphene.String, required=True))

    node = relay.Node.Field()

    def resolve_streets(self, args, context, info):
        return Street.objects.all()

    def resolve_search(self, args, context, info):
        term = args['q']
        people = Person.objects.filter(name__icontains=term)
        houses = House.objects.annotate(name=Concat(F('number'), Value(' '), F('street__name'), output_field=models.TextField())).filter(name__icontains=term)
        streets = Street.objects.filter(name__icontains=term)
        return itertools.chain(people, houses, streets)


schema = graphene.Schema(query=Query)
