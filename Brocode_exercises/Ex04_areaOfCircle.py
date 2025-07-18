import math

# formula A = PI*R**2

radius = float(input("Enter the radius :"))
formula = math.pi * pow(radius,2)

print(f"The area is : {round(formula,2)} cm \n")

