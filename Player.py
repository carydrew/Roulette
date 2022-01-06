class Player:

    def __init__(self, name, money):
        self.name = name.capitalize()
        self.money = money

    def changeMoney(self, money):
        self.money += money

    def dealerCheckMoney(self):
        return self.money

    def currentMoney(self):
        print("{} current has ${}.".format(self.name, self.money))


# Testing

#p1 = Player("bob", 100)
#p1.currentMoney()
#p1.changeMoney(100)
#p1.currentMoney()