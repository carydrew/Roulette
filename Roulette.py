from Dealer import Dealer
from Player import Player

class Roulette:

    rouletteTableNum = 1
    playerNum = 1

    def __init__(self, name, money):
        if money <= 0:
            print("Sorry, you didn't bring enough money to play")
            exit()
        self.gameNum = Roulette.rouletteTableNum
        Roulette.rouletteTableNum += 1
        self.dealer = Dealer(self.gameNum)
        self.player = Player(name, money)

    def play(self):
        play = True
        while play == True:
            winners, losers = self.dealer.getBets(self.player.currentMoney)
            total = self.dealer.payout(winners, losers)
            self.player.changeMoney(total)
            self.player.currentMoney()
            if self.player.money <= 0: 
                print("You ran out of money! Please come back when you have more to play with!")
                break
            again = input("\nWould you like to play again (Y/N): ")
            if again.lower() == "N": break
            else: continue
