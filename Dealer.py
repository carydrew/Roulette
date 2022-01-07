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
            print("Welcome Player! You currently have ${} to play with.".format(top))
            money = int(input("\nHow much do you want to bet? $"))
            bet = input("What is your bet of ${} on? ".format(money))
            newBet = Bet(bet, money)
            # Check if Bet is valid
            if newBet.valid is False: 
                print("Sorry, this bet is allowed. Please make a valid bet.")
                yn = input("Would you like to try another bet (Y/N):  ")
                if yn.upper() == "N": break
                else: continue
            #print("You are betting ${} on {}.".format(money, bet))
            amount += money
            if amount > top:
                amount -= money
                print("Sorry, you don't have enough money for this bet.")
                print("You currently have ${} left to bet with.".format(top-amount))
            else:  betList.append(newBet)
            if amount < top: cont = input("\nAnother Bet (Y/N): ")
            else: break
            if cont.upper() == "N": break
            else: continue
        
        print('\n')
        for bet in betList:
            print("You are betting ${} on {}.".format(bet.amount, bet.pick))
 
        print("\nNo more bets please! I am throwing the ball.")
        time.sleep(3)
        print("\nThe ball is still going.")
        time.sleep(2)
        print("\nThe ball is bouncing!!")
        time.sleep(2)
        self.result = self.table.play(self.strength)

        # self.results looks like
        # {'number': 16, 'color': 'black', 'evenOdd': 'even', 'half': 'first half', 'third': 'second 12', 'column': 'column one'}

        Dealer.sayWinningPossibilities(self, self.result)
        return Dealer.sayWinningBets(self, self.result, betList)

    def sayWinningPossibilities(self, win):

        print("\n\nThe winning items are!")
        for key in win.keys():
            print(win.get(key))

    def sayWinningBets(self, win, betList):
        winnersList = []
        losersList = []
        print("\nThe winning bets placed are: ")
        try:
            for key in win.keys():
                for item in betList:
                    if win.get(key) == item.pick:
                        print("{}".format(item.pick))
                        winnersList.append(item)
                    elif win.get(key) != item.pick: 
                        losersList.append(item)


        except:
            print("\nNo bets won.")

        return winnersList, losersList

    def payout(self, winningBets, losingBets):
        total = 0
        for item in winningBets:
            total += item.win()
        for item in losingBets:
            total -= item.lose()
        
        if total > 0: print("Player, you have won ${}".format(total))
        elif total < 0: print("Player, you have lost ${}".format(total))
        elif total == 0: print("Player, you have lost ${}".format(total))

        return total
    
        
#Testing
#
#d1 = Dealer(1)
#d1.getBets(100)
