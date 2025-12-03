class Book:
    def __init__ (self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
    def get_age(self):
        return 2025 - self.publication_year
    def get_summary(self):
        return f"Title:{self.title}, Author:{self.author},Published year:{self.publication_year}"

book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960)
print(f"Book 3 Title: {book3.title}")
print(f"Book 3 Author: {book3.author}")
print(f"Book 3 Age: {book3.get_age()} years")
print(f"Book 3 Summary: {book3.get_summary()}")