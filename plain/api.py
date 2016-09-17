import itertools

import graphene

from village import population


class Relationship(graphene.Enum):
    parent = 'parent'
    grandparent = 'grandparent'
    child = 'child'
    grandchild = 'grandchild'
    spouse = 'spouse'
    sibling = 'sibling'


class Street(graphene.ObjectType):
    name = graphene.String()
    houses = graphene.List(lambda: House)

    def __init__(self, street):
        self.street = street
        super().__init__()

    def resolve_name(self, args, context, info):
        return self.street.name

    def resolve_houses(self, args, context, info):
        return [House(h) for h in population.houses if h.street == self.street]


class House(graphene.ObjectType):
    street = graphene.Field(Street)
    number = graphene.Int()
    name = graphene.String()
    residents = graphene.List(lambda: Person)

    def __init__(self, house):
        self.house = house
        super().__init__()

    def resolve_street(self, args, context, info):
        return Street(self.house.street)

    def resolve_number(self, args, context, info):
        return self.house.number

    def resolve_name(self, args, context, info):
        return str(self.house)

    def resolve_residents(self, args, context, info):
        return [Person(p) for p in population.people if p.residence == self.house]


class Person(graphene.ObjectType):
    name = graphene.String()
    family = graphene.String()
    residence = graphene.Field(House)
    relationships = graphene.List(lambda: Person, relationship=graphene.Argument(Relationship, required=True))

    def __init__(self, person):
        self.person = person
        super().__init__()

    def resolve_name(self, args, context, info):
        return self.person.name

    def resolve_family(self, args, context, info):
        return self.person.family

    def resolve_residence(self, args, context, info):
        return House(self.person.residence)

    def resolve_relationships(self, args, context, info):
        if args['relationship'] == 'parent':
            return [Person(p) for p in self.person.parents]
        if args['relationship'] == 'grandparent':
            return [Person(gp) for p in self.person.parents for gp in p.parents]
        if args['relationship'] == 'child':
            return [Person(p) for p in population.people if self.person in p.parents]
        if args['relationship'] == 'spouse':
            if self.person.spouse:
                return [Person(self.person.spouse)]
        if args['relationship'] == 'grandchild':
            return [Person(c) for c in population.people if self.person in list(itertools.chain(*[p.parents for p in c.parents]))]
        if args['relationship'] == 'sibling':
            return [Person(p) for p in population.people if sorted(p.parents) == sorted(self.person.parents) and self.person.parents and not p == self.person]
        return []


class Query(graphene.ObjectType):
    people = graphene.List(Person)
    houses = graphene.List(House)
    streets = graphene.List(Street)

    def resolve_people(self, args, context, info):
        return [Person(p) for p in population.people]

    def resolve_houses(self, args, context, info):
        return [House(s) for s in population.houses]

    def resolve_streets(self, args, context, info):
        return [Street(s) for s in population.streets]


schema = graphene.Schema(query=Query)
