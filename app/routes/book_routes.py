from flask import Blueprint
from ..models.book import books

books_bp = Blueprint("books", __name__)

@books_bp.get("/books")
def get_all_books():
    books_response = []

    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return books_response

@books_bp.get("/<id>")
def get_one_book(id):
    id = int(id)
    for book in books:
        if book.id == id:
            book_dict = dict(
                id = book.id,
                title = book.title,
                description = book.description
            )
        return book_dict
