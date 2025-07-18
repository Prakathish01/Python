#Rock Papper Scissors

import random
options = ("rock","paper","scissors")

is_playing = True

while is_playing:
    computer = random.choice(options)
    user = None

    while user not in options:
        user = input("Enter your choice (rock , paper, scissor) :").lower()
        if user not in options:
            print("---------Invalid choice--------")
    print(f"player :{user} ")
    print(f"Computer :{computer}")
    if user == computer:
        print("Its a tie")
    elif user == "rock" and computer =="scissor":
        print("You win!!")
    elif user == "scissor"  and computer == "paper":
        print("You win!!")
    elif user == "paper" and computer == "rock":
        print("You win!!")
    else :
        print("You loss!!")
    again = ("y","n")
    one_more = input("You wanna play again?(Y or N) :").lower()
    while one_more not in again:
        one_more = input("You wanna play again?(Y or N) :").lower()
    if one_more == "n":
        print("Thanks for playing, good bye :)")
        is_playing = False
    elif one_more == "y":
        continue
    else:
        print("invalid comment")
