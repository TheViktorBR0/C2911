import random

print('Welcome to the library of all our projects!')
print('What project you want to see?')
print('Variants: Students life, Cats life, Bank account, Sims, Calculator, AI or Currency converter: ')
choise = input('').lower()

# ---------------------------------------------------------------------------------------------------------------

def Student():
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

def Cat():
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

def Bank():
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

def Sims():
    

# ---------------------------------------------------------------------------------------------------------------
if choise == 'Students life'.lower():

if choise == 'Cats life'.lower():

if choise == 'Bank account'.lower():
