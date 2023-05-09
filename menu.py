from library import Library
from Exceptions import BookAlreadyCheckedOut,BookNotFound

def view_available_books(library):
    available_books = library.get_available_books()
    if available_books:
        print("\nAvailable books:")
        for book in available_books:
            print(f"{book.id}. {book.title} by {book.author}")
        print()
    else:
        print("\nThere are no available books at this time.\n")

def search_books(library):
    query = input("\nEnter your search query (title or author): ")
    results = []
    for book in library.books:
        if query.lower() in book.title.lower() or query.lower() in book.author.lower():
            results.append(book)
    if results:
        print(f"\nSearch results ({len(results)} found):")
        for book in results:
            print(f"{book.id}. {book.title} by {book.author}")
        print()
    else:
        print("\nNo results found.\n")

def check_out_book(library, borrower):
    book_id = input("\nEnter the ID of the book you want to check out: ")
    book = library.find_book_by_id(book_id)
    if book is None:
        raise BookNotFound(f"The book with ID '{book_id}' was not found.")
    elif book.is_checked_out():
        raise BookAlreadyCheckedOut(f"The book '{book.title}' is already checked out.")
    else:
        book.check_out(borrower)
        print(f"\n{book.title} has been checked out by {borrower}.\n")

def return_book(library):
    book_id = input("\nEnter the ID of the book you want to return: ")
    book = library.find_book_by_id(book_id)
    if book is None:
        raise BookNotFound(f"The book with ID '{book_id}' was not found.")
    elif not book.is_checked_out():
        print("\nThis book has not been checked out yet.\n")
    else:
        book.return_book()
        print(f"\n{book.title} has been returned.\n")

def view_borrowing_history(library,borrower):
    borrowing_history = library.get_borrowing_history(borrower)
    if borrowing_history:
        print(f"\nBorrowing history for {borrower}:")
        for book in borrowing_history:
            print(f"{book.id}. {book.title} by {book.author}")
        print()
    else:
        print(f"\nNo borrowing history found for {borrower}.\n")

def print_menu():
    print("\n1. View available books")
    print("2. Search for a book")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. View borrowing history")
    print("6. Exit\n")