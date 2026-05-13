"""
Name: Quoc Huynh
Date Started: 17/11/25
Brief Project Description: A Kivy-based GUI application for managing a reading list. Users can view, sort, add, and update books,
with visual indicators for completed and unread books. The program loads and saves data in "books.json" and demonstrates object-orientated programming (OOP) through the Book and BookCollection classes.
GitHub URL: https://github.com/cp1404-students/a2-books-quochuynh1
"""

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from book import Book
from bookcollection import BookCollection
from kivy.app import App

FILENAME = "books.json"
READ_COLOUR = (.5, .5, 0.5, 1)  # Dark Grey
UNREAD_COLOUR = (0, 1, 1, 1)  # Dark Green
SPINNER_TO_BOOK = {'Title': 'title', 'Author': 'author', 'Pages': 'number_of_pages',
                   'Completed': 'is_completed'}  # maps GUI spinner to the keys that correspond to the Book object attributes


class BooksToReadApp(App):
    """App to keep track of read and unread books"""
    page_count_text = StringProperty()
    bottom_label_text = StringProperty()
    spinner_labels = ListProperty()
    current_spinner = StringProperty()

    def __init__(self, **kwargs):
        """Initialise app, load books from json file and store them in a list of dictionaries"""
        super().__init__(**kwargs)
        self.book_collection = BookCollection()
        self.book_collection.load_books(FILENAME)

    def build(self):
        """Build GUI"""
        self.title = "Books To Read 2.0"
        self.handle_page_count()
        self.bottom_label_text = "Welcome to Books To Read 2.0."
        self.root = Builder.load_file('app.kv')
        self.create_book_buttons()
        self.spinner_labels = SPINNER_TO_BOOK.keys()
        self.current_spinner = 'Author' # Set default sort method
        return self.root

    def create_book_buttons(self):
        """Create buttons from book_collection.books and any user added books"""
        entries_box = self.root.ids.entries_box
        entries_box.clear_widgets()

        for book in self.book_collection.books:
            temp_button = Button(text=str(book))
            temp_button.bind(on_release=self.handle_book_press)
            temp_button.book = book  # Attach book to button
            if book.is_completed:
                temp_button.background_color = READ_COLOUR
            else:
                temp_button.background_color = UNREAD_COLOUR
            entries_box.add_widget(temp_button)

    def handle_book_press(self, instance):
        """Indicate whether a book has been read by changing background colours, notify user via bottom_label_text"""
        book = instance.book
        if book.is_completed:
            book.mark_unread()
            instance.background_color = UNREAD_COLOUR
            if book.is_long():
                self.bottom_label_text = f"You need to read {book.title}. Get Started!"
            else:
                self.bottom_label_text = f"You need to read {book.title}."
        else:
            book.mark_completed()
            instance.background_color = READ_COLOUR
            if book.is_long():
                self.bottom_label_text = f"You completed {book.title}. Great Job!"
            else:
                self.bottom_label_text = f"You completed {book.title}."
        instance.text = str(book)
        self.handle_page_count()
        self.handle_sort(self.current_spinner)

    def handle_page_count(self):
        """Keep a count of how many pages are left to read and display at top of GUI"""
        unread_page_count = self.book_collection.get_unread_pages()
        self.page_count_text = f"Pages to read: {unread_page_count}"

    def handle_sort(self, current_spinner):
        """Sort books depending on which spinner label is selected"""
        self.book_collection.sort(SPINNER_TO_BOOK[current_spinner])
        self.root.ids.entries_box.clear_widgets()
        self.create_book_buttons()

    def get_valid_text_fields(self, title, author, pages):
        """Validate title, author, and year user inputs"""
        title = title.strip()
        author = author.strip()
        pages = pages.strip()

        if title == "" or author == "" or pages == "":
            self.bottom_label_text = "Please complete all fields."
            return False
        try:
            pages = int(pages)
            if pages <= 0:
                self.bottom_label_text = "Book must have some pages!"
                return False
        except ValueError:
            self.bottom_label_text = 'Please enter a valid number.'
            return False
        return title, author, pages

    def add_book(self):
        """Add a new button using the data the user inputted"""
        title = self.root.ids.input_title.text
        author = self.root.ids.input_author.text
        pages = self.root.ids.input_pages.text
        valid_input = self.get_valid_text_fields(title, author, pages)

        if valid_input:
            title, author, pages = valid_input
            new_book = Book(title, author, pages, is_completed=False)
            self.book_collection.add_book(new_book)
            self.handle_sort(self.current_spinner)
            self.create_book_buttons()
            self.handle_page_count()
            self.handle_clear()
            self.bottom_label_text = f"{title} added."


    def handle_clear(self):
        """Clear all input fields as well as bottom_text_label"""
        self.bottom_label_text = ""
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""

    def on_stop(self):
        """Save current book collection in memory to filename upon quitting of Kivy app"""
        self.book_collection.save_books(FILENAME)


if __name__ == '__main__':
    BooksToReadApp().run()
