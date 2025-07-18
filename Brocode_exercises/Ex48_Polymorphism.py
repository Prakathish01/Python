"""
Polymorphism - Greek word that means to "have many forms or faces"
              poly - Many  morphe - Form

              Two ways to achieve polymorphism
              1. Inheritance = An object could be treated of the same type as a parent class
              2. "Duck typing" = Object must have necessary attributes /methods
"""

from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod # decorators
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2
class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius) #Circle.__init__(radius)
        self.topping = topping


shapes =[Circle(5) ,Square(8),Pizza("Chicken",10)]
for shape in shapes:
    print(f"{shape.area()} cm^2")

