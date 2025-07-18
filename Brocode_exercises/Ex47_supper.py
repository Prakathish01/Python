#super()= Function used in a child to call methods from a parent class(superclass)
# ----->Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = "filled" if is_filled else "Not Filled"

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
class Square(Shape):
    def __init__(self,color,is_filled, width):
        super().__init__(color,is_filled)
        self.width = width
circle =Circle("Blue",True,5)
square =Square("red",False,7)

#circle
print(f"It is {circle.color} circle , {circle.is_filled} and {circle.radius} cm radius")
#Square
print(f"It is {square.color} circle , {square.is_filled} and {square.width} cm width")

