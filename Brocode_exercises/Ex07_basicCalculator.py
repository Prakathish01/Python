#Basic Calculator

operator = input("Enter the operator (+,-,*,/) :")
num_1 = float(input("Enter the num_1 :\n"))
num_2 = float(input("Enter the num_2 :\n"))

if operator == "+":
    result = num_1 + num_2
    print(f"The value is {result}")
elif operator == "-":
    result = num_1 - num_2
    print(f"The value is {result}")
elif operator == "*":
    result = num_1 * num_2
    print(f"The value is {result}")
elif operator == "/":
    result = num_1/num_2
    print(f"The value is {result}")
