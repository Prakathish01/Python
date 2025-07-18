#For Loop (range , string , sequence)

name = "Dhanush"
for i in reversed(range(1,10)):
    print(i)
for j in name:
    print(j)
#skip
for k in range(1,25):
    if k%2==1:
        continue
    else :
        print(k)
