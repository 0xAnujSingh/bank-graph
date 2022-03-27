The service is deployed on Heroku and MySQL is used for database.

## Links
* Link: https://anuj-bank-branches.herokuapp.com/gql
* Schema: https://github.com/0xAnujSingh/bank-graph/blob/master/schema.graphql

### `listBank` 

```
query ExampleQuery {
  listBanks {
    banks {
      name
      id
    }
  }
}
```

### `getBank`

```
query ExampleQuery($id: ID!) {
  getBank(id: $id) {
    bank {
      name
    }
  }
}
```

### `getBranch`

```
query ExampleQuery($ifsc: String!) {
  getBranch(ifsc: $ifsc) {
    branch {
      bank {
        name
      }
    }
  }
}
```

