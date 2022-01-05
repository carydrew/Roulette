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

    def __getWheelPosition(self):
        return random.randint(0,36)

    def getResult(self):
        self.ans = random.randint(0,360) + Wheel.__getWheelPosition(self)
        return self.ans % 36

    def __repr__(self):
        ans = Wheel.getResult(self)
        return self.bins[ans]          





#Testing that it makes them all.
#w1 = Wheel()
#print(w1.bins)