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

# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} says woof!")
#
#     def get_age_in_human_years(self):
#         return self.age * 7
#
#
# # Create an instance of the Dog class
# my_dog = Dog("Max", "Golden Retriever", 3)
#
# # Call the bark method
# my_dog.bark()
#
# # Get the age of the dog in human years
# human_age = my_dog.get_age_in_human_years()
# print(f"{my_dog.name} is {human_age} years old in human years.")

#----------------------------------------------------------------------

import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress-= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally...')

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

oleg = Student(name = "Oleg's")

for day in range(365):
    if oleg.alive == False:
        break
    oleg.live(day)

#----------------------------------------------------------------------