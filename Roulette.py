from Dealer import Dealer
from Player import Player

class Roulette:

    rouletteTableNum = 1

    def __init__(self, name, money):
        self.gameNum = Roulette.rouletteTableNum
        Roulette.rouletteTableNum += 1
        self.dealer = Dealer(self.gameNum)
        self.player = Player(name, money)
