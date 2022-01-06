import random

class Dealer:

    def __init__(self, num):
        self.strength = random.randrange(1,100)
        self.tableAssigned = num

    def __repr__(self):
        pass

    def getThrowStrength(self):
        return self.strength