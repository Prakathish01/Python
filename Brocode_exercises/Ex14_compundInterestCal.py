# Compound Interest Calculator
# Formula A=P(1+r/n)^t

principle = 0
time = 0
rate = 0

while principle <=0:
    principle = float(input("Enter the amount:"))
    if principle<= 0:
        print("Please enter the right amount")

while time<=0:
    time = float(input("Enter the time:"))
    if time <=0:
        print("Please Enter the right time period!")

while rate <= 0:
    rate = float(input("Enter the rate"))
    if rate <= 0:
        print("Please Enter the right rate1")

Interest = principle * pow((1 + rate / 100 ),time)
print(f"Balance after {time} year/s: ${Interest :.2f}")