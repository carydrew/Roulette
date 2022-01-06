import random
from Bin import Bin


class Wheel:
    
    tableNum = 1

    def __init__(self):
        self.tableNum = Wheel.tableNum
        Wheel.tableNum += 1
        self.bins = []
        for x in range(0,37):
             self.x= Bin(x)
             self.bins.append(self.x)

    def _getWheelPosition(self):
        self.position = random.randint(0,36)

    def spin(self):
        Wheel._getWheelPosition(self)
        self.res = (random.randint(0,360) + self.position) % 36
        return self.bins[self.res].getResults()

    #def __repr__(self):
    #    Wheel.spin(self)
    #    self.winner = self.bins[self.res].getResults()
    #    return self.winner


#testing

#w1 = Wheel()
#print(w1.spin())