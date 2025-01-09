class Book:
    def __init__(self, title, author, num_of_pages):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages

    def __eq__(self, other):
       return self.title == other.title or self.author == other.author or self.num_of_pages == other.num_of_page
    
    def __lt__(self, other):
        return self.num_of_pages > other.num_of_pages
    
    def __gt__(self, other):
        return self.num_of_pages < other.num_of_pages
    
    def __add__(self, other):
        return self.num_of_pages + other.num_of_pages
    
    def __sub__(self, other):
        return self.num_of_pages - other.num_of_pages
    
    def __contains__(self, key):
        return key in self.title or key in self.author
    
    def __str__(self):
        return f"{self.title} is book of {self.author} having {self.num_of_pages} pages."

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philospher", "J.K. Rowling", 310)
book3 = Book("The Lion, Witch and The Wardobe", "C.S. Lewis", 173)
print(book3)