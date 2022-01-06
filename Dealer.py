import random
from Bet import Bet
from Table import Table
import time


class Dealer:

    def __init__(self, num):
        self.strength = random.randrange(1,100)
        self.tableAssigned = num
        self.table = Table(self.tableAssigned)

    def getThrowStrength(self):
        return self.strength

    def getBets(self, top):
        betnum = 0
        betList = []
        more = True
        amount = 0
        while more == True:
            bet = input("\nWhat is your bet on? ")
            money = int(input("How much do you want to bet? $"))
            #print("You are betting ${} on {}.".format(money, bet))
            amount += money
            if money > top:
                print("Sorry, you don't have enough money for this bet.")
                more = False
                break
            betList[betnum] = Bet(bet, money)
            cont = input("\nAnother Bet (Y/N): ")
            if cont.upper() == "N":
                more = False
                break
        
            for bet in betList:
                print("You are betting ${} on {}. The odds are {}:1".format(bet.bet, bet.amount,bet.odds))
        
        print("\nNo more bets please! I am throwing the ball.")
        time.sleep(3)
        print("\nThe ball is still going.")
        time.sleep(2)
        print("\nThe ball is bouncing!!")
        time.sleep(2)
        self.result = self.table.play(self.strength)

        print("\n\nThe winning items are!")
        for key in self.result.keys():
            print()
    
        
        for bet in betList:
