from Roulette import Roulette

def main():
       print('''Hello! Welcome the Roulette Casino. In this you will 
       be able create multiple tables of Roulette to play with.
       It is up to you on how many games you want to play at a time.
                     Enjoy the Game! 
              This was created by Cary Drew.''')

       name = input("What is your name?  ")
       money = int(input("How much money did you bring to play with? $"))

       if money <= 0: 
              print("Sorry, you didn't bring any money to play!")
              exit()


       print("Hello {}! Hopefully you leave with more than you brought!!\n\n".format(name.capitalize()))

       r = Roulette(name, money)
       r.play()

       print("Thanks for playing!")

if __name__ == '__main__':
       main()
        
