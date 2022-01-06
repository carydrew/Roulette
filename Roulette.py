from Game import Game


print('''Hello! Welcome the Roulette Casino. In this you will 
be able create multiple tables of Roulette to play with.
It is up to you on how many games you want to play at a time.
                 Enjoy the Game! 
          This was created by Cary Drew.''')

name = input("What is your name?  ")
money = int(input("How much money did you bring to play with? $"))

print("Hello {}! Hopefully you leave with more than ${}!".format(name, money))
