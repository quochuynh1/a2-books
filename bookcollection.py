"""Assignment 2 BookCollection class"""

import json
from operator import attrgetter

from book import Book


class BookCollection:
    """Manage a collection of Book objects"""

    def __init__(self):
        """Initialise the BookCollection with an empty list of books"""
        self.books = []

    def __str__(self):
        """Return a string representation of books"""
        return f"{self.books}"

    def __repr__(self):
        return str(self)

    def load_books(self, filename):
        """Load books from JSON file into Book objects in the list"""
        with open(filename, "r") as in_file:
            book_data = json.load(in_file)

        for record in book_data:
            book = Book(title=record["title"], author=record["author"], number_of_pages=record["number_of_pages"],
                        is_completed=record["is_completed"])
            self.books.append(book)

    def add_book(self, book):
        """Add a Book object to the books collection"""
        self.books.append(book)

    def sort(self, key):
        """Sort the collection by the key passed in, then by title"""
        self.books.sort(key=attrgetter(key, "title"))

    def get_unread_pages(self):
        """Return total number of unread pages"""
        return sum(book.number_of_pages for book in self.books if not book.is_completed)

    def get_completed_pages(self):
        """Return total number of completed pages"""
        return sum(book.number_of_pages for book in self.books if book.is_completed)

    def save_books(self, filename):
        """Save books to books.json"""
        books_to_save = []

        for book in self.books:
            books_to_save.append({"title":book.title, "author":book.author, "number_of_pages":book.number_of_pages, "is_completed":book.is_completed})

        with open(filename, "w") as out_file:
            json.dump(books_to_save, out_file)