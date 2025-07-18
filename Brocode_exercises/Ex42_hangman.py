# Hangman

import random

fruits = ("apple", "banana", "mango", "orange", "grape")

hangman_art = {
    0: """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    1: """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    2: """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    3: """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    4: """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    5: """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    6: """
     +---+
     |   |
    😵   |
    /|\\  |
    / \\  |
         |
    =========
    """
}

def display_man(wrong_guesses):
    print(hangman_art[wrong_guesses])
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(fruits)
    hint = ["_"] * len(answer)
    wrong_guesses =0
    guessed_letter = set()
    is_running = True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter the letter :").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input!!")
            continue
        if guess in guessed_letter:
            print(f"Already guessed :'{guess}'")
            continue
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
                    guessed_letter.add(guess)
        else:
            wrong_guesses +=1
        if "_" not in hint:
            print("-------------------------------")
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) -1:
            print("-------------------------------")
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lost!")



if __name__ =="__main__":
    main()