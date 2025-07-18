"""
@Property - Decorator used to define a method as a property (it can be accessed like a attribute)
            Benefit : Add additional logic when read , write or delete attributes
            Gives you getter , setter and deleter method
"""
class Rectangle:

    def __init__(self,width,height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")
rectangle = Rectangle(4,5)
rectangle.width = 3

del rectangle.height
print(rectangle.width)

