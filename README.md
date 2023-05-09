Book class: A class representing a book with an id, title, author, and borrower attribute.
Library class: A class representing a library that contains a list of books and methods to manage the books.
add_book(title, author): A method of the Library class that adds a new book to the library.
remove_book(id): A method of the Library class that removes a book from the library by its ID.
get_book(id): A method of the Library class that retrieves a book from the library by its ID.
get_books(): A method of the Library class that retrieves all the books in the library.
get_available_books(): A method of the Library class that retrieves all the available books in the library.
get_borrowed_books(): A method of the Library class that retrieves all the borrowed books in the library.
get_borrowing_history(borrower): A method of the Library class that retrieves the borrowing history of a borrower.
check_out_book(id, borrower): A method of the Library class that allows a borrower to check out a book from the library by its ID.
return_book(id): A method of the Library class that allows a borrower to return a book to the library by its ID.
view_books(books): A function that prints out a list of books.
view_borrowing_history(library): A function that allows a borrower to view their borrowing history from the library.