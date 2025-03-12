import random

rand_num = random.randint(1, 100)

guess = ""


while (guess != rand_num):
    try:
        guess = int(input('Guess the number between 1 and 100: '))
        if (guess > rand_num):
                print("Too high!")
        elif (guess < rand_num):
                print("Too low!")
        else:
            print("Congratulations! You guessed the number")

        
            
    except ValueError:
        print("Please enter a valid number")