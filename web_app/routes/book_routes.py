# web_app/routes/book_routes.py

from flask import Blueprint, jsonify

# import from init file
book_routes = Blueprint("book_routes", __name__)


# attach route to bluprint object
@book_routes.route('/books.json') # home page
def books():
    print("Visit Book Page")
    # fake database
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)
