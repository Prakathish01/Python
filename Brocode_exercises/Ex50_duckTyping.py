"""
Duck typing - Another way of achieving Polymorphism besides Inheritance
              Object must have the minimum necessary attributes/methods
              "If it looks like a duck and quacks like a dock , it must be duck
"""
class Animal:
    is_alive =True

class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    def speak(self):
        print("Honk")

speaks = [Dog(),Cat(),Car()]

for _ in speaks:
    _.speak()