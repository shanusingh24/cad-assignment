from flask import Flask , jsonify, request

app = Flask(__name__)

books = [
    {'id':1,'name':'book_1','author':'author_1'},
    {'id':2,'name':'book_2','author':'author_2'},
    {'id':3,'name':'book_3','author':'author_3'},
    {'id':4,'name':'book_4','author':'author_4'}

]

# This is our Home page. 
@app.route('/Home',methods=['GET'])
def home_page():
    return "This is my Home _page"

# This page will show all our books data. 
@app.route('/Home/books',methods=['GET'])
def book_data():
    return jsonify(books)

# This page will show us single book data. 
@app.route('/Home/books/<int:book_id>',methods=['GET'])
def single_book(book_id):
    for book in books:
        if book['id'] == book_id :
            return jsonify(book)
    return jsonify({'message':'Book not found'})

# This will add a new book. 
@app.route('/Home/books',methods=['POST'])
def add_book():
    new_book = {
        'id' : request.json['id'],
        'name' : request.json['name'],
        'author' : request.json['author']
    }
    books.append(new_book)
    return jsonify({'message':'Book added Succesfully'})

# This will update an existing book data.
@app.route('/Home/books/<int:book_id>',methods = ['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id :
            book['name'] = request.json['name']
            book['author'] = request.json['author']
            return jsonify({'message':'Book updated Succesfully'})
    return jsonify({'message':'Book not found'})

# This will Delete an existing book data.
@app.route('/Home/books/<int:book_id>',methods = ['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message":"Book Deleted Succesfully"})
    return jsonify({'message':'Book not found'})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)