from Dealer import Dealer
from Table import Table
from Player import Player

class Game:

    gameNum = 1

    def __init__(self):
        self.gameNum = Game.gameNum
        Game.gameNum += 1
        self.dealer = Dealer(self.gameNum)
        self.table = Table(self.gameNum)






        
