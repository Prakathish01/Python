#Fibonocci of the Nth number
num = int(input("Enter the number:"))


# a,b =0,1
# till = int(input("Enter the number:"))
# for i in range(till):
#     a,b = b,b+a
# print(b-a)

def fibNth(num):
    if num <2:
        return num
    return fibNth(num-1) + fibNth(num-2)
print(fibNth(num - 1))
