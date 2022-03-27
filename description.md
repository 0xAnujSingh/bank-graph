# ADVERTYZEMENT_ASSIGNMENT


# Run Locally
Python Version: 3.9.7

Requirements:
```
MySQLdb
csv
flask
Ariadne Library
```

### `import.py`
In this file, data is fetched by using `csv`. And creating a tables named bank and branch. After fetching data, data is insert into tables.

### `__init__.py`
In this file, we are start flask server. Adding our database url into it.

<!-- ### `models.py`
In this file, we are creating a tables named bank and branch. -->

### `schema.graphql`
This file describes the shape of our data. This is the core of any graphql server. This file defines the functionality available to the client application that consumes the API.  

### `main.py`
In this file, I am wire up our server with graphql, so that we can start using the queries which is defined in schema.   

### `queries.py`
This file is responsible for populating the data for a single field in our schema. Whenever a client queries for a particular field, the resolver for that field fetches the requested data from the appropriate data source.