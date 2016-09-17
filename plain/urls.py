from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django_graphiql.views import GraphiQL

from .api import schema

urlpatterns = [
    url(r'^graphql/', csrf_exempt(GraphQLView.as_view(schema=schema))),
    url(r'^graphiql/', GraphiQL.as_view(graphql_url='/simple/graphql/')),
]
