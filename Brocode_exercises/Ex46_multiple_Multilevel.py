# Multiple inheritance = inherit from more than one parent class C(A,B)
# Multi-Level inheritance = inherit from one parent which inherit from another parent
# C(B) <- b(A) <- A

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def fleeing(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator): # --> Multiple Inheritance
    pass

rabbit = Rabbit("Kumar")
fish = Fish("Ranjith")
hawk = Hawk("Kathi")

rabbit.fleeing()
fish.fleeing()
fish.hunt()

rabbit.sleep()