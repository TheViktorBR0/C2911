#----------------------------------------------------------------------

# class Book:
#     amount_of_books = 0
#     def __init__(self, color = 'I am red book -_-'):
#         self.color = color
#         Book.amount_of_books += 1
#
# books = Book()
# first_book = Book(color = 'And i am blue book -_-')
# second_book = Book(color = 'And i am blue book -_-')
#
# print(books.color)
# print(second_book.color)
#
# print(books.amount_of_books, 'Book(s)')
# print(Book.amount_of_books, 'Book(s)')

#----------------------------------------------------------------------

# class Book:
#     def __init__(self):
#         self.length -= 1
#     length = 40
#     def printer(self):
#         print(self.length)
#
# book = Book()
#
# book.printer()

#----------------------------------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to read')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress-= 0.1

#----------------------------------------------------------------------