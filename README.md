# Roulette
A more difficult class based version of Roulette. Rather than the 1 function version in my GamesOfChances repository. 


# Instructions:
- The program starts from Game.py. This is the only file you will actually need to open and start. The other files will need to be in the same directory to be imported correctly.
- The only imports are time and rand. So no pip requirements.


# Classes overview.

Game class:
    Starts the game. Takes in the name and starting money of the player. 
    Starts the roulette file and game logic. 

Roulette class:
    The initial init will set the player/dealer/table info.
    The program will then call the play() method which has the logic to continue playing.
    The game will end if the player quits or runs out of money. 
    This imports Dealer and Player classes.
        - Dealer controls game flow, taking of bets and payouts.

Player Class:
    Takes in the player name and initial money. Tracks money based on bets. 
    Gets accessed by the Dealer class to update money. 

Dealer Class: 
    This is the largest class of all. Each dealer is assigned a table with the variable of tablenum that is passed from the roulette class.
    When init it will assign a random "strength" to emulate how each dealer will throw the ball with a different force.
    The main method is the getBets() which does the following:
        1. Gets bets, up to the max amount of money a player has.
        2. Validate bets, eg. can't bet on 37 because it doesn't exist. 
        3. Spins the ball, annouces it's been thrown and it is still going.
        4. States what number the ball landed on and all the possible winners with that. This is done by calling the sayWinningPossibilities() method.
        5. States what bets made actually won via the sayWinningBets() method. 
            - This will also return a list of the instances of bets that won and a total value of bets that did not win.
    The roulette class will then call the payout() method which will add together the winning bets and losing bets for the player and change the players currentmoney value. 
    This class imports the Table and Bet classes.

Table Class: 
    Takes in a table number, creates the table associated with that number. It should be the same number assigned to the dealer. This is then passed to wheel class to create the wheel assoicated with the table. 
    Has a play() method that will call for the will to be spun.

Wheel class:
    Creates the 38 bins for the wheel via the Bin class.
    The getResult() function has a random number start for the wheel position, similar to the wheel spining consistently in real life. 
        Then it adds in another random int to similate the ball throw.
        Uses Modulo to get the number it would land on.  

Bin class:
    Takes in a number and can return a dict of that holds all the variable associated with the possible wins. Such as color, even or odd, etc. 

    Has a getResults() method that will return the dict of the bets that would win if that bin was the one the ball landed in.

Bet class:
    This is called via the Dealer class.
    Takes in the int:bet_amount and a string/int for a bet. 
    This will have variables holding the bet, the amount betted, the amount returned if won (called from the outcome class) and a check that the bet is valid using a bool function. 
    Win() method will return an int of the amount bet x the odds(aka the amount you win as it isn't really the exact odds of winning).
    Lose() method will return a negative value of the amount bet.
    valid() method checks to see if the bet is an acceptable item to bet on.
    Imports Outcome to get the odds.


Outcome class:
    Takes in a variable and set a variable with the variable name and the odds (aka the amount won) if that bet wins. For example: if a single number is bet on and wins, it would win 35:1. So if I bet a $1, I would win $35. 

Future thoughts. 
- Expand the game to include creation of multiple players.
    - I am thinking this just needs to be done by making the bets list into a dict. The name of the person making the bet is the key and then the value is a list of the bet instances. 
- Add a gui to point and click on bets. Make it easier to bet on items that you don't have to type. 


