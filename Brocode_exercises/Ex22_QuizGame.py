#Python quiz Game

questions = ("How many elements are there in periodic table",
             "Which animal lays the largest egg",
             "what is the most abundant gas in the earth atmosphere")
options = (("A . 116","B. 117" ,"C. 118", "D. 119"),
           ("A.Whale", "B.Crocodile", "C.Elephant", "D. Ostrich"),
           ("A.Nitrogen","B.Oxygen","C.carbon dioxide","D.Hydrogen" ))
answers = ("C","D","A")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("--------------------------")
print("       Result             ")
print("--------------------------")

print("answers : ", end="")
for answer in answers:
    print(answer , end=" ")
print()

print("guesses :",end="")
for guess in guesses:
    print(guess , end=" ")
print()

score = int(score / len(questions) * 100)

print(f"your score is {score}")
