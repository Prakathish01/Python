"""
Decorator - A function that extends the behaviour of another function
            w/o modifying the base function
            Pass the base function as an argument to the decorator
"""

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("You added Sprinkles")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
def iceCream(flavor):
    print(f"Get your {flavor} icecream!!")

# iceCream = add_sprinkles(iceCream) # Manual method
iceCream("Vanila")

