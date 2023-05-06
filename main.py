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
            print()
            for passengers in self.passengers:
                print()
