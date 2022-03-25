from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import getBranchBank_resolver, listBanks_resolver, getBank_resolver, getBankBranch_resolver, getBranch_resolver

query = ObjectType("Query")
query.set_field("listBanks", listBanks_resolver)
query.set_field("getBank", getBank_resolver)
query.set_field("getBranch", getBranch_resolver)

bankQuery = ObjectType("Bank")
bankQuery.set_field("branches", getBankBranch_resolver)

branchQuery = ObjectType("Branch")
branchQuery.set_field("bank", getBranchBank_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, bankQuery, branchQuery, snake_case_fallback_resolvers
)

@app.route("/gql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code