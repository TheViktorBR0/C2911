import random
import cv2
from PIL import Image
import requests

print("=============================================")
print('   Welcome to the library of my projects!')
print("=============================================")
print('What project you want to see?')
print("Variants: Student's life, Cat's life, Bank account, Sims, Calculator, AI or Currency converter: ")
choise = input("").lower()

# ---------------------------------------------------------------------------------------------------------------

def student():
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
            self.progress -= 0.1

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

    oleg = Student(name="Oleg's")

    for day in range(365):
        if oleg.alive == False:
            break
        oleg.live(day)

# ---------------------------------------------------------------------------------------------------------------

def cat():
    class Cat:
        def __init__(self, name):
            self.name = name
            self.sleep = 20
            self.eat = 0
            self.pet = 1
            self.alive = True

        def to_eat(self):
            print('Time to eat')
            self.eat += 0.12
            self.sleep -= 5

        def to_sleep(self):
            print('Time to sleep')
            self.sleep += 3
            self.eat -= 0.1
            self.pet -= 0.05

        def to_pet(self):
            print('Time to pet me')
            self.sleep += 5
            self.pet += 0.1

        def is_alive(self):
            if self.eat < -0.5:
                print('Needed to eat more, but 8 more lives left!')
                self.alive = False
            elif self.sleep <= 0:
                print('Needed to sleep more, but 8 more lives left!')
                self.alive = False
            elif self.eat > 5:
                print('Needed to eat less, but 8 more lives left!')
                self.alive = False
            elif self.pet < 0.8:
                print('Needed to pet more, but 8 more lives left!')
                self.alive = False

        def end_of_day(self):
            print(f"sleep = {self.sleep}")
            print(f"eat = {round(self.eat, 2)}")
            print(f"pet = {round(self.pet, 2)}")

        def live(self, day):
            day = "Day " + str(day) + " of " + self.name + " life"
            print(f"{day:=^100}")
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_eat()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_pet()
            self.end_of_day()
            self.is_alive()

    cat = Cat(name="cat's")

    for day in range(365):
        if cat.alive == False:
            break
        cat.live(day)

# ---------------------------------------------------------------------------------------------------------------

def bank():
    class BankAccount:
        def __init__(self, account_number, balance):
            self.account_number = account_number
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            print(f"Deposit of {amount} successful. Current balance is {self.balance}")

        def withdraw(self, amount):
            if amount > self.balance:
                print("Withdrawal failed. Not enough funds.")
            else:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful. Current balance is {self.balance}")

        def get_balance(self):
            return self.balance

    account_number = int(input("Enter account number: "))
    balance = float(input("Enter starting balance: "))

    my_account = BankAccount(account_number, balance)
    print(f"Account number: {my_account.account_number}")
    print(f"Current balance: {my_account.get_balance()}")

    deposit_amount = float(input("Enter deposit amount: "))
    withdrawal_amount = float(input("Enter withdrawal amount: "))

    my_account.deposit(deposit_amount)
    my_account.withdraw(withdrawal_amount)
    print(f"Current balance: {my_account.get_balance()}")

# ---------------------------------------------------------------------------------------------------------------

def sims():
    import random

    class Human:
        def __init__(self, name='Human', job=None, home=None, car=None):
            self.name = name
            self.money = 100
            self.gladness = 50
            self.satiety = 50
            self.job = job
            self.car = car
            self.home = home

        def get_home(self):
            self.home = House()

        def get_car(self):
            self.car = Auto(brands_of_cars)

        def get_job(self):
            if self.car.drive():
                pass
            else:
                self.to_repair()
                return
            self.job = Job(job_list)

        def eat(self):
            if self.home.food <= 0:
                self.shopping('food')
            else:
                if self.satiety >= 100:
                    self.satiety = 100
                    return
                self.satiety += 5
                self.home.food -= 5

        def work(self):
            if self.car.drive():
                pass
            else:
                if self.car.fuel < 20:
                    self.shopping('fuel')
                    return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

        def shopping(self, manage):
            if self.car.drive():
                pass
            else:
                if self.car.fuel < 20:
                    manage = 'fuel'
                else:
                    self.to_repair()
                    return
            if manage == 'fuel':
                print('I bought fuel')
                self.money -= 100
                self.car.fuel += 100
            elif manage == 'food':
                print('I bought food')
                self.money -= 50
                self.home.food += 50
            elif manage == 'delicacies':
                print('I bought delicacies')
                self.money -= 15
                self.gladness += 10
                self.satiety += 2

        def chill(self):
            self.gladness += 10
            self.home.mess += 5

        def clean_home(self):
            self.gladness -= 5
            self.home.mess = 0

        def to_repair(self):
            self.car.strength += 100
            self.money -= 50

        def days_indexes(self, day):
            day = f" Today the {day} of {self.name}'s life"
            print(f"{day:=^50}", "\n")

            human_indexes = self.name + "'s indexes"
            print(f"{human_indexes:^50}", "\n")
            print(f"Money - {self.money}")
            print(f"Satiety - {self.satiety}")
            print(f"Gladness - {self.gladness}")

            home_indexes = "Home indexes"
            print(f"{home_indexes:^50}", "\n")
            print(f"Food - {self.home.food}")
            print(f"Mess - {self.home.mess}")

            car_indexes = f"{self.car.brand} car indexes"
            print(f"{car_indexes:^50}", "\n")
            print(f"Fuel - {self.car.fuel}")
            print(f"Strength - {self.car.strength}")

        def is_alive(self):
            if self.gladness < 0:
                print("Depression...")
                return False
            elif self.satiety < 0:
                print("Dead...")
                return False
            elif self.money < -500:
                print("Bankrupt...")
                return False

        def live(self, day):
            if self.is_alive() == False:
                return False
            if self.home is None:
                print("Settled in the house")
                self.get_home()
            if self.car is None:
                self.get_car()
                print(f"I bought a car {self.car.brand}")
            if self.job is None:
                self.get_job()
                print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
            self.days_indexes(day)
            dice = random.randint(1, 4)

            if self.satiety < 20:
                print("I'll go eat")
                self.eat()
            elif self.gladness < 20:
                if self.home.mess > 15:
                    print("I want to chill, but there is so much mess... \n So i will clean the house")
                    self.clean_home()
                else:
                    print("Let's chill")
                    self.chill()
            elif self.money < 0:
                print("Start working")
                self.work()
            elif self.car.strength < 15:
                print("I need to repair my car")
                self.to_repair()
            elif dice == 1:
                print("Let's chill")
                self.chill()
            elif dice == 2:
                print("Start working")
                self.work()
            elif dice == 3:
                print("Clean time")
                self.clean_home()
            elif dice == 4:
                print("Time for treats!")
                self.shopping(manage='delicacies')

    class Auto:
        def __init__(self, brand_list):
            self.brand = random.choice(list(brand_list))
            self.fuel = brand_list[self.brand]['fuel']
            self.strength = brand_list[self.brand]['strength']
            self.consumption = brand_list[self.brand]['consumption']

        def drive(self):
            if self.strength > 0 and self.fuel >= self.consumption:
                self.fuel -= self.consumption
                self.strength -= 1
                return True
            else:
                print('The car cannot move')
                return False

    class House:
        def __init__(self):
            self.mess = 0
            self.food = 0

    job_list = {
        'Java developer': {'salary': 50, 'gladness_less': 10},
        'Python developer': {'salary': 40, 'gladness_less': 3},
        'C++ developer': {'salary': 45, 'gladness_less': 25},
        'Rust developer': {'salary': 70, 'gladness_less': 1},
    }

    brands_of_cars = {
        'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
        'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
    }

    class Job:
        def __init__(self, job_list):
            self.job = random.choice(list(job_list))
            self.salary = job_list[self.job]['salary']
            self.gladness_less = job_list[self.job]['gladness_less']

    nick = Human(name='Nick')

    for day in range(1, 8):
        if nick.live(day) == False:
            break

# ---------------------------------------------------------------------------------------------------------------

def calculator():
    def checker(*exc_types):
        def checker(function):
            def checker(*args, **kwargs):
                try:
                    result = function(*args, **kwargs)
                except (exc_types) as exc:
                    print(f"We have a problems {exc}")
                else:
                    print(f"No problems. Result - {result}")

            return checker

        return checker

    @checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
    def calculate(expression):
        return eval(expression)

    calculate(input('Enter calculation: '))

# ---------------------------------------------------------------------------------------------------------------

def ai():
    image_path = 'cat.jpg'
    cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    image = cv2.imread(image_path)

    cat_face = cat_face_cascade.detectMultiScale(image)

    cat = Image.open(image_path)
    glasses = Image.open('glasses.png')
    cat = cat.convert('RGBA')

    for (x, y, w, h) in cat_face:
        glasses = glasses.resize((w, int(h / 3)))
        cat.paste(glasses, (x, int(y + h / 4)), glasses)
        cat.save('cat_with_glasses.png')
        cat_with_glasses = cv2.imread('cat_with_glasses.png')
        cv2.imshow('cat_with_glasses.png', cat_with_glasses)
        cv2.waitKey()

    # ------------------------------------------------------------------

    image_path = 'dog.jpg'
    dog_face_cascade = cv2.CascadeClassifier('dog_face.xml')
    image = cv2.imread(image_path)

    dog_face = dog_face_cascade.detectMultiScale(image)

    dog = Image.open(image_path)
    bubble = Image.open('bubble.png')
    dog = dog.convert('RGBA')

    for (x, y, w, h) in dog_face:
        bubble = bubble.resize((w, int(h / 1.4)))
        dog.paste(bubble, (x, int(y + h / 1.5)), bubble)
        dog.save('dog_with_bubble.png')
        dog_with_glasses = cv2.imread('dog_with_bubble.png')
        cv2.imshow('dog_with_bubble.png', dog_with_glasses)
        cv2.waitKey()

# ---------------------------------------------------------------------------------------------------------------

def currency():
    responce = requests.get('https://finance.i.ua/')

    responce_text = responce.text

    responce_parse = responce_text.split('<span>')

    print('Print a price with hryvnias(₴): ')
    price = input()

    for parse_elem1 in responce_parse:
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2[1].isdigit():
                cours = float(price) / float(parse_elem2)
                print("Rounded price in dollars($) is: ")
                print(round(cours, 2), '$')
                quit()

# ---------------------------------------------------------------------------------------------------------------

if choise == "Student's life".lower():
    student()
    print('-----------------------------')
    print('Thanks for using our library!')
    print('-----------------------------')

elif choise == "Cat's life".lower():
    cat()
    print('-----------------------------')
    print('Thanks for using our library!')
    print('-----------------------------')

elif choise == "Bank account".lower():
    bank()
    print('-----------------------------')
    print('Thanks for using our library!')
    print('-----------------------------')

elif choise == "Sims".lower():
    sims()
    print('-----------------------------')
    print('Thanks for using our library!')
    print('-----------------------------')

elif choise == "Calculator".lower():
    calculator()
    print('-----------------------------')
    print('Thanks for using our library!')
    print('-----------------------------')

elif choise == "AI".lower():
    ai()
    print('-----------------------------')
    print('Thanks for using our library!')
    print('-----------------------------')

else:
    print("That variant isn't possible!")
    quit()