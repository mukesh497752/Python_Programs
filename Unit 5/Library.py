class Library:

    def __init__(self):
        self.books = ["Python", "Java", "C Programming"]

    def display_books(self):
        print("Available Books:", self.books)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "borrowed successfully")
        else:
            print("Book is not available")


    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")


# Creating object
lib = Library()

# Display available books
lib.display_books()

# Borrow a book
lib.borrow_book("Python")

# Display books after borrowing
lib.display_books()

# Return a book
lib.return_book("Python")

# Display books after returning
lib.display_books()