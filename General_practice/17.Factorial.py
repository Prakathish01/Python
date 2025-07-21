#Factorial of the number
from math import factorial

num = int(input("Enter the number:"))

# Using for loop

# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)

#using recursive Function

def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)
print(factorial(num))