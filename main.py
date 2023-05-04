import random

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

cat = Cat(name = "cat's")

for day in range(365):
    if cat.alive == False:
        break
    cat.live(day)