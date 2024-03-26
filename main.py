from flask import Flask, render_template

app = Flask(__name__)

title = "Book List"

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "description": "A novel about American Dream.",
    },
    {
        "id": 2,
        "title": "Harry Potter: and The Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "description": "The book is about 11 year old Harry Potter, who receives a letter saying that he is invited to attend Hogwarts, school of witchcraft and wizardry. He then learns that a powerful wizard and his minions are after the sorcerer's stone that will make this evil wizard immortal and undefeatable.",
    },
    {
        "id": 3,
        "title": "Sherlock Holmes: A Study in Scarlet",
        "author": "Arthur Conan Doyle",
        "year": 1887,
        "description": "The story marks the first appearance of Sherlock Holmes and Dr. Watson, who would become the most famous detective duo in literature.",
    },
]


@app.route("/")
def book_list():
    return render_template("book_list.html", title=title, books=books)


@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return render_template("book_detail.html", book=book)
    else:
        return "Book not found", 404


if __name__ == "__main__":
    app.run(debug=True)
