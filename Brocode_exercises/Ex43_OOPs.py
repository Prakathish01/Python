# Object -> A "bundle" of related attributes (variables) and methods (functions)
# Ex, phone , cup , book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color

    def describe(self):
        return f"This player has a '{self.model}' car, {self.color} color, and {self.year} edition."

player1 = Car("Toyota Innova",2024,"Grey")
player2 = Car("Mustang","2022","red")

print(player1.describe())
print(player2.describe())

"""
-----------> For the understanding of "Self"
class numb:
    a =10
    def another(self,a):
        self.a = a
        return a
i = numb()
print(i.a) -->10
print(i.another(100)) ---->100
print(i.a) --->100
"""

