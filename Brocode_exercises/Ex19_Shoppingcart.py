#Shopping Cart

items=[]
prices=[]
total = 0

while True:
    item = input("Enter the required food items(q for quit):")
    if item.lower()=="q":
        break
    items.append(item)
    price = float(input("Price of the item:$"))
    prices.append(price)
print("The items are:")
item_count = len(items)
for i in range(item_count):
    print(f"{items[i]} : {prices[i]:>}")
for j in prices:
    total += j
print(f"The total cost of these items are : ${total}")

# for i in items:
#     print(i,end=" ")
# print()
# for j in prices:
#     total += j
#     print(j,end=" ")