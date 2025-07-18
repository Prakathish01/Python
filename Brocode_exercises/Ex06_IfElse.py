#Age verification
import math
Age = math.floor((float(input("Enter the age :\n"))))
print(Age)
if Age >= 18:
    print("You are eligible ")
elif Age<0:
    print("Born first nigga")
else :
    print("You are not eligible")