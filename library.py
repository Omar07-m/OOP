from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author)
        self.books.append(book)

    def find_book_by_id(self, book_id):
        for book in self.books:
            if str(book.id) == book_id:
                return book
        return None

    def get_available_books(self):
        available_books = []
        for book in self.books:
            if not book.is_checked_out():
                available_books.append(book)
        return available_books

    def get_borrowing_history(self, borrower):
        borrowing_history = []
        for book in self.books:
            if book.borrower == borrower:
                borrowing_history.append(book)
        return borrowing_history