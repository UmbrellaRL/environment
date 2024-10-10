"""Business logic for resolving GraphQL queries/mutations."""

from core import testing_strawberry
from api.graphql.types import Book

async def get_books() -> list[Book]:
    return testing_strawberry.get_books()

# Mutation example
# async def create_user(username: str) -> str:
#     # Call business logic here
#     return f"User {username} created!"

# Dep Inj example
# async def create_user(username: str, db=Depends(get_db)) -> str:
#     # Use db to create the user
#     return f"User {username} created in DB!"

