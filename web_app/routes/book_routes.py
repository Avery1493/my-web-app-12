# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, render_template, request

# import from init file
book_routes = Blueprint("book_routes", __name__)


# attach route to bluprint object
@book_routes.route('/books.json') # home page
def list_books():
    print("Request Books JSON Page")
    # fake database
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)

@book_routes.route('/books') # home page
def books():
    print("Visit Book Page")
    # fake database
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("books.html", books=books) 
    # return html file located in templates
    # passing books variable to page
    # view using jinja language

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")

