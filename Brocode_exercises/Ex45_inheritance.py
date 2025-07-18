#Inheritance

#--->Allows a class to inherit attributes and methods from another class
#--->Helps with code resuability and extensibility
#--->class Child/parent

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    speak = "Woof"
class Cat(Animal):
    speak = "Meow"
class Mouse(Animal):
    speak = "Squeek"

dog = Dog("Tony")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(mouse.name)
dog.eat()
mouse.eat()
cat.sleep()
print(dog.speak)
print(cat.speak)
print(mouse.speak)
