"""
Refactoring Assignment 1 - Books
to use Book and BookCollection classes
"""

from book import Book
from bookcollection import BookCollection

FILENAME = "books.json"
COMPLETED = "c"
UNREAD = False


def main():
    """Program to keep track of books to read"""

    book_collection = BookCollection()
    book_collection.load_books(FILENAME)

    print("Books to Read 2.0 by Quoc Huynh")
    print(f"{len(book_collection.books)} books loaded.")

    print("Menu: ")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "D":
            print_books(book_collection)
        elif choice == "A":
            add_books(book_collection)
        elif choice == "C":
            complete_books(book_collection)
        else:
            print("Invalid menu choice")
        print("Menu: ")
        print("D - Display books")
        print("A - Add a new book")
        print("C - Complete a book")
        print("Q - Quit")
        choice = input(">>> ").upper()
    save_books(FILENAME, book_collection)
    print('"So many books, so little time. Frank Zappa"')


def load_book_data(filename):
    """Load book information as a list of lists for other functions to access"""
    with open(filename, "r") as in_file:
        book_data = [line.strip().split(",") for line in in_file]
        return book_data


def save_books(filename, book_collection):
    """Save all books to books.csv upon quitting program"""
    book_collection.save_books(filename)


def print_books(book_collection):
    """Print the book data as well as how many pages and books are still left to be read"""
    total_unread_books, total_unread_pages = format_print_books(book_collection)
    determine_no_more_books_to_read(total_unread_books, total_unread_pages)


def format_print_books(book_collection):
    """Format the way the books print so that they align neatly"""
    total_unread_pages = 0
    total_unread_books = 0

    books = book_collection.books

    max_name_length = max(len(book.title) for book in books)
    max_author_length = max(len(book.author) for book in books)
    max_page_length = max(len(str(book.number_of_pages)) for book in books)

    for line_number, book in enumerate(books, 1):

        book_name = book.title
        author = book.author
        number_of_pages = book.number_of_pages
        book_status = book.is_completed

        if book_status == UNREAD:
            print(
                f"*{line_number:}. {book_name:{max_name_length}} by {author:{max_author_length}} {number_of_pages:{max_page_length}} pages")
            total_unread_pages += number_of_pages
            total_unread_books += 1
        else:
            print(
                f"{line_number:>2}. {book_name:{max_name_length}} by {author:{max_author_length}} {number_of_pages:{max_page_length}} pages")
    return total_unread_books, total_unread_pages


def determine_no_more_books_to_read(total_unread_books: int, total_unread_pages: int):
    """Notify if there are no more books to read and suggest to add a new book"""
    if total_unread_books == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still need to read {total_unread_pages} pages in {total_unread_books} books")


def add_books(book_collection):
    """Add new book data"""
    title = get_non_empty_input("Title: ")
    author = get_non_empty_input("Author: ").title()
    number_of_pages = get_valid_int("Number of Pages: ")

    new_book = Book(title, author, number_of_pages, is_completed=False)
    book_collection.add_book(new_book)
    print(f"{title} by {author} ({number_of_pages} pages) added.")


def get_non_empty_input(prompt) -> str:
    """Prompt the user to enter input until it is not empty. """
    user_input = input(prompt).strip()
    while user_input == "":
        print("Input can not be blank")
        user_input = input(prompt).strip()
    return user_input


def get_valid_int(prompt):
    """Prompt the user to enter a number until it is valid"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                is_valid_input = True
                return number
        except ValueError:
            print("Invalid input - please enter a valid number")
    return None


def complete_books(book_collection):
    """Prompt the user to select a book to mark as completed and update its status accordingly"""
    if no_unread_books(book_collection):
        return
    else:
        print_books(book_collection)
        print("Enter the number of a book to mark as completed")
        mark_book_as_completed(book_collection)


def mark_book_as_completed(book_collection):
    """Mark the book the user indicates as completed if in range and not already"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = get_valid_int(">>> ")
            book = book_collection.books[number - 1]
            if book.is_completed:
                print("That book is already completed")
            else:
                book.mark_completed()
                print(f"{book.title} by {book.author} completed!")
                is_valid_input = True
        except IndexError:
            print("Invalid book number")


def no_unread_books(book_collection):
    """Check if all books in the list are already completed"""
    if all(book.is_completed == COMPLETED for book in book_collection.books):
        print("No unread books - well done!")
        return True
    return False


if __name__ == '__main__':
    main()
