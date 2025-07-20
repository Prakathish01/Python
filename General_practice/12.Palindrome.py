#Palindrome
"""
def palindrome(num,rev=0):
    if num < 0:
        return False
    else:
        temp = num
        for i in range(len(str(num))):
            rem = temp%10
            rev = rev*10 + rem
            temp= temp // 10
        return rev == num
print(palindrome(1221))
"""
def palindrome(num,rev=0):
    if num == 0:
        return 0
    else:
        rem =num %10
        rev = rev*10 + rem
        return palindrome(num//10,rev)
num = int(input("Enter the num :"))
rev = palindrome(num)
print("Palindrome") if rev == num else print("Not Palindrome")
