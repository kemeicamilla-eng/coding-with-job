class LibraryBook:
    def __init__(self, title, author, isbn, year):
        self.year = year
        self.available = True
        self.title = title

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Title: {self.title}, Author: {self.author}")
        else:
            print("This book is not available for borrowing.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Title: {self.title}, Author: {self.author}")
        else:
            print("This book was not borrowed.")

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.year}, Availability: {availability}")
        