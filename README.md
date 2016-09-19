# An introduction to Graphene and Relay

This is the supporting material for a tutorial on Graphene and Relay.

## Set up

### Customizing the database

You can also customize the database used with the `DATABASE_URL` environment var
(thanks to [dj-database-url](https://github.com/kennethreitz/dj-database-url)),
if not PostgreSQL will be used as default.

```bash
export DATABASE_URL='sqlite://test.db'
```

### Migrate

Set up the models in the database with `python manage.py migrate`.


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
