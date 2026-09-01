# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's build-in operations.
#                 They allow developer to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author 
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found!"

book1 = Book("Game of Throns", "R.R. Martin", 200)
# book2 = Book("Game of Throns", "R.R. Martin", 200)
book2 = Book("House of The Dragon", "R.R. Martin", 400)
book3 = Book("The Hobbit", "J.J.R. Tolkien", 400)

# print(book1)
# print(book2)
# print(book3)
# print(book1 == book2)
# print(book1 < book2)
# print(book1 + book2)
# print("Game" in book1)
# print("Martin" in book2)
print(book1['title'])
print(book3['author'])
print(book3['audio'])