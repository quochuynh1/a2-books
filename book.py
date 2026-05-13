"""Assignment 2 Book class"""


class Book:
    """Represent a Book object"""

    def __init__(self, title="", author="", number_of_pages=0, is_completed=False):
        """Initialise a Book instance"""
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_completed = is_completed

    def __str__(self):
        """Return a string representation of the book data"""
        if self.is_completed:
            return f"{self.title} by {self.author}, {self.number_of_pages} pages (completed)"
        else:
            return f"{self.title} by {self.author}, {self.number_of_pages} pages"

    def __repr__(self):
        return str(self)

    def mark_completed(self):
        """Mark book as completed"""
        self.is_completed = True

    def mark_unread(self):
        """Mark book as unread"""
        self.is_completed = False

    def is_long(self):
        """Determine if the book is considered long (long books are >= 500 pages)"""
        if self.number_of_pages >= 500:
            return True
        return False
