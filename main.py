from library import Library
from menu import *


if __name__=='__main__':
    library = Library()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")
    library.add_book("Pride and Prejudice", "Jane Austen")

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_available_books(library)
        elif choice == "2":
            search_books(library)
        elif choice == "3":
            borrower = input("\nEnter your name: ")
            check_out_book(library, borrower)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            borrower = input("\nEnter your name: ")
            view_borrowing_history(library, borrower)
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")
