#Shopping cart program

item = input("Which item you want to buy :\n")
quantity = int(input("Tell us the quantity:\n"))
cost = int(input("cost of the product :\n"))

total_amount = quantity*cost

print(f"The total amount of {quantity} {item} is :{total_amount}")