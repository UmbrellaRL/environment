from api.graphql.types import Book

def get_books() -> list[Book]:
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]
