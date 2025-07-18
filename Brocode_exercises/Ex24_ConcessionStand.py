# Concession Stand

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade":4.25}
cart = []
total = 0

print("-----------MENU--------------")
for key, value in menu.items():
        print(f"{key:10} : ${value : .2f}")
print("-----------------------------")

while True:
        food = input("Select the food you want (q for quit):").lower()
        if food=="q":
                break
        elif menu.get(food) is not None:
                cart.append(food)
print()
print("----------your cart---------")
for item in cart:
        total += menu.get(item)
        print(f"{item:10} : ${menu.get(item):.2f}")
print(f"Total cost is :${total}")
print("----------------------------")

