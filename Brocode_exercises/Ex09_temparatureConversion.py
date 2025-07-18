# Temperature Conversion

# Celsius to Fahrenheit F = (C * 9/5) + 32
# Fahrenheit to Celsius C = (F -32) * 5/9

unit = input("is the temperature in Fahrenheit or celsius (F OR C) :\n ")

temp = float(input("Enter the temperature :\n"))

if unit == "C" :
    result = round(((9* temp ) /5) + 32,1)
    print(f"The converted temperature is {result} F")
elif unit == "F":
    result = round((temp-32) *5/9,1)
    print(f"The converted temperature is {result} C")
else :
    print("The unit is incorrect")






