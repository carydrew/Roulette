import random
from Bin import Bin


class Wheel:
    
    def __init__(self, tableNum):
        self.tableNum = tableNum
        self.bins = []
        for x in range(0,37):
             self.x= Bin(x)
             self.bins.append(self.x)

    def _getWheelPosition(self):
        self.position = random.randint(0,36)

    def spin(self, num):
        Wheel._getWheelPosition(self)
        self.res = (random.randint(0,360) + self.position + num) % 36
        return self.bins[self.res].getResults()

    #def __repr__(self):
    #    Wheel.spin(self)
    #    self.winner = self.bins[self.res].getResults()
    #    return self.winner


#testing

#w1 = Wheel(1)
#print(w1.spin(1))