from Outcome import Outcome

class Bet:

    
    def __init__(self, bet, amount: int):
        self.pick = bet
        self.amount = amount
        self.odds = Outcome(bet)
        self.valid = Bet.valid(self, bet)

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

    def valid(self, bet):
        validList = ['red','black','odd','even', 'first 12', 'second 12', 'third 12', 'first half', 'second half', 'column one', 'column two', 'column three']

        if bet in range(0,37):
            return True
        elif bet in validList:
            return True
        else: return False

    
#Testing

# b1 = Bet("black", 100)
# b2 = Bet("red", 100)
# b1.printWinLossAmount("black")
# b2.printWinLossAmount("black")





