# Even Or Odd

def is_what(number):
    return not number&1 # we convert if it gives 1
number = int(input("Enter the number:"))
if is_what(number):
    print("Even")
else:
    print("Odd")

#print("Even") if number%2==0 else print("Odd")


