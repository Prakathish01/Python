#-----------Prime--------------

num = int(input("Enter the number :\n"))
flag =0
# if num <2:
#     flag = 1
# else :
#     for i in range(2,int(pow(num,0.5))):
#         if num%i ==0:
#             flag = 1
#             break
# print("Prime" if flag ==0 else "Not Prime")

if num < 2:
    flag = 1
elif num==2:
    flag =0
for i in range(3,int(pow(num,0.5)),2):
    if num % i ==0:
        flag = 1
        break
print("Prime" if flag ==0 else "Not Prime")