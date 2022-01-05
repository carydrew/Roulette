class Bin:

    def __setColor(self):
        if self.number == (0 or 00):
            self.color = None
        elif self.number == (1 or 3 or 5 or 7 or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 30 or 32 or 34 or 36):
            self.color = "red"
        else:
            self.color = "black"
    
    def __setEvenOdd(self):
        if self.number == (0 or 00):
            self.eo = None
        elif self.number % 2 == 0:
            self.eo = 'even'
        else:
            self.eo = 'odd'

    def __setHalf(self):
        if self.number == (0 or 00):
            self.half = None
        elif self.number > 0 and self.number <= 18:
            self.half = 'first half'
        else:
            self.half = 'second half'
    
    def __setThirds(self):
        if self.number == (0 or 00):
            self.third = None
        elif self.number >=1 and self.number <= 12:
            self.third = "first 12"
        elif self.number >=13 and self.number <= 24:
            self.third = "second 12"
        else: 
            self.third = 'third 12'
    
    def __setColumn(self):
        if self.number == (0 or 00):
            self.column = None
        elif self.number % 3 == 1:
            self.column = "column one"
        elif self.number % 3 == 1:
            self.column = "column two"
        else:
            self.column = "column three"
    def __init__(self, num: int):
        self.number = num
        Bin.__setColor(self)
        Bin.__setColumn(self)
        Bin.__setEvenOdd(self)
        Bin.__setHalf(self)
        Bin.__setThirds(self)

        
    def __repr__(self):
        if self.number == (0 or 00):
            return "The number is {}".format(self.number)
        else:
            return "The number is {}, {} {} {} {} {}".format(self.number,self.eo,self.column,self.half,self.color,self.third)

    def getResults(self):
        if self.number == (0 or 00):
            results = {"number": self.number}
        else:
            results = {"number": self.number,"color":self.color ,"evenOdd": self.eo, "half": self.half, "third":self.third,"column":self.column}
        return results

# test

#b1 = Bin(1)
#print(b1)
#print(b1.getResults())

#b2 = Bin(0)
#print(b2)
#print(b2.getResults())

# the double 00 doens't work :( 

#b3 = Bin(00)
#print(b3)
#print(b3.getResults())