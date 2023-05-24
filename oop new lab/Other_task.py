class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return True
        return False

    def search_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]


import unittest

class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book 1", "Author 1")
        self.book2 = Book("Book 2", "Author 2")
        self.book3 = Book("Book 3", "Author 1")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_add_book(self):
        book4 = Book("Book 4", "Author 3")
        self.library.add_book(book4)
        self.assertIn(book4, self.library.books)

    def test_borrow_book(self):
        self.assertTrue(self.library.borrow_book("Book 1"))
        self.assertFalse(self.library.borrow_book("Book 1"))  # Already borrowed
        self.assertFalse(self.library.borrow_book("Book 4"))  # Book not found

    def test_return_book(self):
        self.assertFalse(self.library.return_book("Book 1"))  # Not borrowed
        self.library.borrow_book("Book 1")
        self.assertTrue(self.library.return_book("Book 1"))

    def test_search_by_title(self):
        books = self.library.search_by_title("Book 1")
        self.assertEqual(len(books), 1)
        self.assertIn(self.book1, books)

        books = self.library.search_by_title("Book 4")  # Book not found
        self.assertEqual(len(books), 0)

    def test_search_by_author(self):
        books = self.library.search_by_author("Author 1")
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book3, books)

        books = self.library.search_by_author("Author 3")  # Author not found
        self.assertEqual(len(books), 0)

if __name__ == '__main__':
    unittest.main()