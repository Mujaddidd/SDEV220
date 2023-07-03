from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []

class Book(Resource):
    def get(self, book_id):
        for book in books:
            if book['id'] == book_id:
                return jsonify(book)
        return {'message': 'Book not found'}, 404

    def post(self, book_id):
        book_name = request.json['book_name']
        author = request.json['author']
        publisher = request.json['publisher']

        book = {'id': book_id, 'book_name': book_name, 'author': author, 'publisher': publisher}
        books.append(book)
        return book, 201

    def put(self, book_id):
        for book in books:
            if book['id'] == book_id:
                book['book_name'] = request.json['book_name']
                book['author'] = request.json['author']
                book['publisher'] = request.json['publisher']
                return book, 200
        book_name = request.json['book_name']
        author = request.json['author']
        publisher = request.json['publisher']

        book = {'id': book_id, 'book_name': book_name, 'author': author, 'publisher': publisher}
        books.append(book)
        return book, 201

    def delete(self, book_id):
        for index, book in enumerate(books):
            if book['id'] == book_id:
                books.pop(index)
                return {'message': 'Book deleted'}, 200
        return {'message': 'Book not found'}, 404

class BookList(Resource):
    def get(self):
        return jsonify(books)

api.add_resource(Book, '/book/<int:book_id>')
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    app.run(debug=True)