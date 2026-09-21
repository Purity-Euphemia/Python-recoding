class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print("Reading", self.title)


book1 = Book("Python for Beginners", "John")

print(book1.title)
print(book1.author)

book1.read()