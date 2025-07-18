#Weight converter
# 1 kilogram = 2.205 pounds

unit = input("Kilogram or pounds (K or L): \n").upper()
weight = float(input("Enter the weight :"))

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
else :
    print("Wrong unit")
print(f"The weight of the person is {round(weight,1)} {unit}")

