#Number Guessing Game

import random
import math

lowest_num = 1
highest_num =100
guesses = 0
still_guessing = True
ans = random.randint(lowest_num,highest_num)

while still_guessing:
    guess = input(f"Enter the valid number between {lowest_num} and {highest_num} (type 'ans' for answer):")
    if guess == "ans":
        print(f"You lost , the answer is {ans}")
        still_guessing =False
    elif guess.isdigit():
        guess = int(guess)
        guesses +=1
        if lowest_num < guess > highest_num:
            print("Please enter valid Number between the range !!")
        elif guess > ans :
            print("High, take another guess")
        elif guess < ans :
            print("Low, take another guess")
        else :
            print("----------------------------------------------")
            print(f"You, got the answer '{guess}' ")
            print(f"you took {guesses} guesses to find the answer")
            print("----------------------------------------------")
            still_guessing = False
