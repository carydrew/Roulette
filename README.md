# Roulette
A more difficult class based version of Roulette. Rather than the 1 function version in my GamesOfChances repository. 


Bin class:
    Takes in a number and can return a dict of all possible wins for it.

Wheel class:
    Creates the 38 bins for the wheel. 
    The getResult() function has a random number start for the wheel position, similar to the wheel spining consistently in real life. 
        Then it adds in another random int to similate the ball throw. 
        Uses Modulo to get the number it would land on. 
        ** Future will add a strength function to the ball from the dealer to have each dealer throw differently. 

Outcome class:
    Takes in a number or string from the wheel/bin class and then will return the odds. 

Bet class:
    Takes in the bet. Returns the value of the bet after the win. 

Player Class:
    Takes in the player name and initial money. Tracks money based on bets. 