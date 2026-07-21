class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies   # added line
        self.available_copies = total_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book borrowed successfully.")
        else:
            print("No copies available.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print("Book returned successfully.")
        else:
            print("All copies are already in the library.")

    def display_details(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Available Copies: {self.available_copies}")  # added line


# test scenario
book1 = Book(201, "Python Programming", "Pavan kumar", 5)

book1.display_details()

book1.borrow_book()
book1.borrow_book()

book1.display_details()

book1.borrow_book()
book1.borrow_book()

book1.return_book()

book1.display_details()