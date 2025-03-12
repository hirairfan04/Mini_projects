import random

choice = ""

class Dice():
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2

while choice.upper() != 'N':
    choice = input('Roll the dice? (y/n): ')
    if choice.upper() == 'Y':
        d = Dice()
        print(d.roll())
        
    else:
        print("Invalid choice!")
else:
    print("Thanks for playing!")