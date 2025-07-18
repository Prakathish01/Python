"""
Abstraction - It used to show only the template of the program
(only the necessary things eg, Switch box)
abc - abstract base class
"""

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def moveForward(self):
        pass
    @abstractmethod
    def moveBackward(self):
        pass

class Car(Vehicle):

    def moveForward(self):
        print("Vehicle is moving forward")
    def moveBackward(self):
        print("Vehicle is moving backward")

car = Car()

car.moveForward()
car.moveBackward()