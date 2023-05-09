from Exceptions import BookAlreadyCheckedOut


class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.checked_out = False
        self.borrower = None

    def is_checked_out(self):
        return self.checked_out

    def check_out(self, borrower):
        if self.checked_out:
            raise BookAlreadyCheckedOut(f"The book '{self.title}' is already checked out.")
        self.checked_out = True
        self.borrower = borrower

    def return_book(self):
        self.checked_out = False
        self.borrower = None