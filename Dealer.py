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
        betList = []
        more = True
        amount = 0
        while more == True:
            money = int(input("\nHow much do you want to bet? $"))
            bet = input("What is your bet of ${} on? ".format(money))
            newBet = Bet(bet, money)
            # Check if Bet is valid
            if newBet.valid == False: 
                print("Sorry, this bet is allowed. Please make a valid bet.")
                continue
            #print("You are betting ${} on {}.".format(money, bet))
            amount += money
            if amount > top:
                amount -= money
                print("Sorry, you don't have enough money for this bet.")
                print("You currently have ${} left to bet with.".format(top-amount))
            else:  betList.append(newBet)
            if amount < top: cont = input("\nAnother Bet (Y/N): ")
            else: cont = "N"
            if cont.upper() == "N":
                print('\n')
                for bet in betList:
                    print("You are betting ${} on {}.".format(bet.amount, bet.pick))
                more = False
                break
        
            
        
        print("\nNo more bets please! I am throwing the ball.")
        time.sleep(3)
        print("\nThe ball is still going.")
        time.sleep(2)
        print("\nThe ball is bouncing!!")
        time.sleep(2)
        self.result = self.table.play(self.strength)

        # self.results looks like
        # {'number': 16, 'color': 'black', 'evenOdd': 'even', 'half': 'first half', 'third': 'second 12', 'column': 'column one'}

        print("\n\nThe winning items are!")
        for key in self.result.keys():
            print(self.result.get(key))

        print("\nThe winning bets placed are: ")
        try:
            pass
        finally:
            print("No bets won.")
    
        
#Testing
#
d1 = Dealer(1)
d1.getBets(100)
