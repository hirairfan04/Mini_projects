import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

emojis = {
        ROCK : "🥌",
        PAPER : "📰",
        SCISSOR : "✂"
    }

options = tuple(emojis.keys())

def user_input():
    choice = input("Rock, paper or scissor? (r/p/s): ")
    return choice

def comp_input():
    comp_choice = random.choice(options)
    return comp_choice

def print_choices(choice, comp_choice):
    user = emojis.get(choice)
    comp = emojis.get(comp_choice)
    print(f"You choose {user}")
    print(f"Computer choose {comp}")

def det_winner(choice, comp_choice):
    if (choice == comp_choice):
        print("Draw!")
    elif ((choice == ROCK and comp_choice == SCISSOR)or
            (choice == PAPER and comp_choice == ROCK)or
            (choice == SCISSOR and comp_choice == PAPER)):
        print("You win!")
    else:
        print("You lose!")


def game():
    while True:

        choice = user_input()
        comp_choice = comp_input()

        if (choice in options):
            print_choices(choice, comp_choice)
            det_winner(choice, comp_choice)
        else:
            print("Invalid choice!!!")
            continue
        
        to_cont = input("Continue? (y/n): ")
        if(to_cont.lower() == 'n'):
            break

game()