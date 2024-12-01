from graphene import ObjectType, String, Schema, List, Field

class Book(ObjectType):
    title = String()
    author = String()

    def resolve_title(root, info):
        return root.title

    def resolve_author(root, info):
        return root.author

books = [
    Book(title="Cien Años de Soledad", author="Gabriel García Márquez"),
    Book(title="Don Quijote de la Mancha", author="Miguel de Cervantes"),
]

# Defining queries
class Query(ObjectType):
    all_books = List(Book)
    book_by_title = Field(Book, title=String(required=True))

    def resolve_all_books(root, info):
        return books

    def resolve_book_by_title(root, info, title):
        return next((book for book in books if book.title == title), None)

# Create the GraphQL schema
schema = Schema(query=Query)

if __name__ == "__main__":
    query = """
    {
        allBooks {
            title
            author
        }
        bookByTitle(title: "Cien Años de Soledad") {
            title
            author
        }
    }
    """
    result = schema.execute(query)
    print(result.data)
