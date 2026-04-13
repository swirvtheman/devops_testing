# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

books = []
next_id = 1


@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)


@app.route("/api/books", methods=["POST"])
def create_book():
    global next_id
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "title and author required"}), 400
    book = {
        "id": next_id,
        "title": data["title"],
        "author": data["author"],
    }
    next_id += 1
    books.append(book)
    return jsonify(book), 201


@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    data = request.get_json()
    if "title" in data:
        book["title"] = data["title"]
    if "author" in data:
        book["author"] = data["author"]
    return jsonify(book)


@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
