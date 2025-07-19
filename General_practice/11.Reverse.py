# Reverse String

# word = input("Enter the word:")
# print(word[::-1])

# print(word[::1]) ----print the odd value
#print(word[::-2]) --------	Take every second element backward
#print(word[::2])---------- Take every second element forward

#Reverse number

def num(n,rev=0):
    return rev if n ==0 else  num(n//10, (rev*10)+(n%10))
print(num(int(input("Enter the number:\n"))))


