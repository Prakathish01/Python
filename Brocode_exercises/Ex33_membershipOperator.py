#Membership Operator
#--->Used to test the value is in the sequence or not(string , tuple, list , set or the dictionary)
# 1.in 2.not in

word = "kumar"
fruits = ["Apple","Bannana","Orange","Pineapple"]
user_input = input("Guess the letter present in the word: \n")
fruit = input("Guess the fruit:\n").capitalize()
if user_input not in word:
    print("Wrong guess :( ")
else:
    print(f"Got it {user_input} ")
if fruit not in fruits:
    print("Its wrong guess")
else:
    print(f"{fruit} correct guess")
capitals = {"Usa" : "washington DC",
            "India" : "New Delhi",
            "Russia" : "Moscow"}

capital = input("Enter the capital name :\n").capitalize()

if capital in capitals:
    print(f"The capital of {capital} is {capitals[capital]}")
else:
    print("The country you entered is not in the list!")
