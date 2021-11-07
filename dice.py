#Beginner projects - Dice Rolling Simulator

from random import randint

dice = [1,2,3,4,5,6]

def roll():
    rolling = True
    count = 0
    
    while rolling :
        if count == 0:
            print('Hello welcome to my dice roller! \nChoose between 1 and 10 dice to roll or say quit to exit')
        else :
            print('\nRolling again...\n\nChoose between 1 and 10 dice to roll or say quit to exit')
        inp = input('How many would you like to roll?')
        if(inp == 'quit') :
            rolling = False
        else :
            die = []
            try :
                num = int(inp)
            except:
                print('Invalid input')
                count = count + 1
                continue    
            if(num > 10) :
                print('Maximum number exceeded')
                count = count + 1
                continue
            else :
                for i in range(num):
                    roll = randint(0,5)
                    rolled = dice[roll]
                    die.append(rolled)
                print('You rolled a', die)
                count = count + 1

roll()
print('Thanks for playing!')
quit()