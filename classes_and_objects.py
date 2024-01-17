class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_information(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

# Create an instance of the Book class
my_book = Book(title="Why Hitler was Right", author="FUHRER", genre="History")

# Display information about the book
my_book.display_information()

# Update information directly
my_book.title = "2 States"
my_book.author = "Chetan Bhagat"
my_book.genre = "Drama,Romance"

# Display updated information
my_book.display_information()
