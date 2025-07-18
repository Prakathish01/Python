#Logical operators
# AND /OR/ NOT

num = int(input("Enter the number:"))

if num > 10 and num <= 15 :
    print(f"You got good marks : {num} / 15")
elif num <=5 or num <= 0 :
    print(f"you got fail marks : {num}/15")
else :
    print(f"Invalid mark")
