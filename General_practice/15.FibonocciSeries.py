#Fibonocci Series

a,b =0,1
till = int(input("Enter the number:"))
for i in range(till):
    print(a,end=" ")
    a,b = b,b+a

