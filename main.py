class Book:
    print("I am book -_-")
    def __init__(self):
        self.color = 'red'
        print("And i am red -_-")

first_book = Book
Book.__init__(self=first_book)