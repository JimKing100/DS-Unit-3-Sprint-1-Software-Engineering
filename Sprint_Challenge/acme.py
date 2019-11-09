#  Imports

import random


# Create the class
class Product:
    # Define the constructor with the instance attributes
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.id = random.randint(1000000, 9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    # Create the greets method
    def stealability(self):
        price_weight = self.price / self.weight
        if price_weight < 0.5:
            print('Not so stealable')
        else:
            if (price_weight >= 0.5 and price_weight < 1.0):
                print('Kinda stealable')
            else:
                print('Very stealable')

    def explode(self):
        flame_weight = self.flammability * self.weight
        if flame_weight < 10:
            print('...fizzle')
        else:
            if (flame_weight >= 10 and flame_weight < 50):
                print('...boom!')
            else:
                print('...BABOOM!')


class BoxingGlove(Product):
    # Define the constructor with the instance attributes
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print('That tickles')
        else:
            if (self.weight >= 5 and self.weight < 15):
                print('Hey that hurt!')
            else:
                print('OUCH!')
