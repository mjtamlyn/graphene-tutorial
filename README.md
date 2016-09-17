# An introduction to Graphene and Relay

This is the supporting material for a tutorial on Graphene and Relay.

## Data model

The data model is of a little (fictional!) welsh village. There are 3 streets,
with 10 houses. People live in the houses and are related to each other. People
can get married, have children and move house.

We have an application should allow you to explore the village and find out
about the people who live there, and update the data as they move, marry, have
children and so on.

## Website structure

The `village` directory is the Django project folder.

The `plain` directory contains a simplistic, database free implementation of
the data model, and a simple graphene API.

The `relay` directory contains a Relay-compliant, Django database model backed
implementation of the data model.

The `application` directory contains a full Relay application.
