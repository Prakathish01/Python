#Find the Greatest of the Three Numbers in Python

num1 =int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
max =0

max = num1 if num1 >num2 else num2
max = num3 if num3 > max else max
print("Greatest of three number is : %d",max)