# Formula C = Root of a^2 +b^2

import math

a = float(input("Enter the value of a :\n"))
b = float(input("Enter the value of b :\n"))
C = math.sqrt(pow(a,2)+pow(b,2))

print(f"The value is :{round(C,2)}\n")