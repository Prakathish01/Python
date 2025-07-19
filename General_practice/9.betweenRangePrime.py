low,high = 2,25
prime = [2,3]

for i in range(low,high+1):
    flag = 0
    if i < 2:
        flag = 1
    elif i % 2==0 or i % 3==0:
        continue
    iter = 5
    while iter <= int(pow(i,0.5)):
        if i % iter ==0:
            flag = 1
            break
        iter += 2
    if flag == 0 :
        prime.append(i)
print(prime)

