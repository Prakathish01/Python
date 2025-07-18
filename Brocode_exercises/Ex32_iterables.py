#iterables

# import time
# for i in reversed(range(1,6)):
#     print(i,sep="-")
#     time.sleep(1)

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade":4.25}
print("-----------MENU--------------")
for key, value in menu.items():
        print(f"{key:10} : ${value : .2f}")
print("-----------------------------")