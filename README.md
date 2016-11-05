# An introduction to Graphene and Relay

This is the supporting material for a tutorial on Graphene and Relay.  For the
slides, check out this [speaker deck](https://speakerdeck.com/mjtamlyn/an-introduction-to-graphene-and-relay)

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

## Getting started

To run this application locally, use the following steps:

- **Clone this repository and pip install requirements**

- **Migrate and populate your new village**
From the root directory of the project:

```
./manage.py migrate
./manage.py create_village
```

N.B.  This tutorial uses a basic sqlite database. You can change `settings.py`
to use a different [dj_database_url](https://github.com/kennethreitz/dj-database-url)
config instead.  

- **Start Making Queries**

```
./manage.py runserver
```

Go to `http://127.0.0.1:8000/plain/graphql` or 
`http://127.0.0.1:8000/relay/graphql` to interact with the API using GraphiQL

- **Optional Step: Build JavaScript package**
```
npm install
npm run build
```