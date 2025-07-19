# Sum of digit

#recursion

# def sum(n):
#     return 0 if n==0 else int(n%10) + sum(n/10)
# num = int(input("Enter the number:\n"))
# print(sum(num))

i = list(map(int,input("Enter the number:\n").strip()))
print(sum(i))