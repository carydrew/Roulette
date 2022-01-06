from Outcome import Outcome

class Bet:

    
    def __init__(self, bet, amount: int):
        self.bet = bet
        self.amount = amount
        self.odds = Outcome(bet)

    def winOrLoss(self, res):
        if res == self.bet:
            return (self.amount * self.odds.odds)
        else:
            return (self.amount * -1) 

    def printWinLossAmount(self,res):
        ans = Bet.winOrLoss(self, res)
        if ans < 0:
            print("You lost ${}.".format(ans))
        else:
            print("You won ${}!".format(ans))

    
#Testing

# b1 = Bet("black", 100)
# b2 = Bet("red", 100)
# b1.printWinLossAmount("black")
# b2.printWinLossAmount("black")





