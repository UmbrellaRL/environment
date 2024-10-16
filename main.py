"""FastAPI module."""

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api.graphql.schema import schema

graphql_app = GraphQLRouter(schema=schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
