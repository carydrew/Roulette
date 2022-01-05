import random

class Dealer:

    def __init__(self):
        self.strength = random.randrange(1,100)

    
    def __repr__(self):
        pass

    def getThrowStrength(self):
        return self.strength