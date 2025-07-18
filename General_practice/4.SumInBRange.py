#Find the Sum of Numbers in a given Range in Python

#Recursion
num1 = int(input("Enter the num 1:"))
num2 = int(input("Enter the num 2:"))
total = 0
#Formula -----------------------------------------
def func(num1,num2):
    N = num2 - num1 +1
    return N * (num1+num2) // 2
print(f"Output : {func(num1,num2)}")
#Recursion ---------------------------------------
# def sum(total,num1,num2):
#     if num1 > num2:
#         return total
#     return num2 + sum(total,num1,num2-1)
# print(sum(total,num1,num2))
