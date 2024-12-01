# GraphQL in Python

A simple GraphQL API implementation using Graphene in Python for managing a book collection.

## Description

This project demonstrates a basic GraphQL API that provides queries for retrieving book information. It includes functionality to fetch all books and search for specific books by title.

## Features

- GraphQL Schema with Book type definition
- Query support for retrieving all books
- Query support for finding books by title
- Sample data with classic literature books

## 📋 Prerequisites

- Python 3.6 or higher
- Graphene library

## 🛠 Installation

1. Install the required dependencies:
```bash
pip install graphene
```

2. Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd <project-directory>
```

## 🚀Usage

Run the script:
```bash
python books.py
```

### Example Queries

Fetch all books:
```graphql
{
    allBooks {
        title
        author
    }
}
```

Find a specific book by title:
```graphql
{
    bookByTitle(title: "Cien Años de Soledad") {
        title
        author
    }
}
```

## 📂 Project Structure

- `Book` class: Defines the GraphQL Object Type for books with title and author fields
- `Query` class: Contains the GraphQL query definitions
- Sample data: Includes two classic Spanish literature books

## Schema Details

### Types

```graphql
type Book {
    title: String
    author: String
}
```

### Queries

- `allBooks`: Returns a list of all books
- `bookByTitle(title: String!)`: Returns a specific book matching the provided title

## Dependencies

- graphene: GraphQL framework for Python
