# 2D Collection

fruits = ["apple", "orange" , "papaya" ,"banana"]
cars = ["ferrari","BWM","jaguar","Toyato"]
bikes = ["RR310","R15","TVS xl","Passion pro"]

randoms = [fruits,cars,bikes]

for random in randoms:
    for rand in random:
        print(rand , end=" ")
    print("")