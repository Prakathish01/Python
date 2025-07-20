#Armstrong
num = int(input("Enter the number:"))
power = len(str(num))
"""
arms =0
temp = num
for i in range(power):
    rem= temp % 10
    arms = pow(rem,power) + arms
    temp = temp//10
print(f"{arms} is Armstrong number") if arms == num else print("Not Armstrong")
"""
def armstrong(num,power,arms=0):
    if num == 0 :
        return arms
    rem=num%10
    arms += pow(rem,power)
    return armstrong(num//10,power,arms)
print("Armstrong" if armstrong( num,power)==num else "Not Armstrong")



