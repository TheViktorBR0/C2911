class Human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

Oleg = Human('Oleg')
Viktor = Human('Viktor')
Mira = Human('Mira')
car = Auto('Folks-vagen')

car.add_passenger(Oleg)
car.add_passenger(Viktor)
car.add_passenger(Mira)
car.print_passengers_names()