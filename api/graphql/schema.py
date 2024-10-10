"""Strawberry Schema"""

import strawberry

from api.graphql.resolvers import get_books
from api.graphql.types import Book


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=get_books)

schema: strawberry.schema = strawberry.Schema(query=Query)
