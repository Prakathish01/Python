#Sum of First N Natural Numbers

number = int(input("Enter the number:"))

"""
Formula - n(n+1)/2
def sum(number):
    return int(number*(number+1)/2)
print(sum(number))
"""
#Loop
"""
sum=0
for i in range(1,number+1):    
    sum += i
print(sum)
"""
# Recursion

def sum(number):
    if number == 0:
        return number
    return number + sum(number-1)
print(sum(number))
