# Polymorphism = Greek word means to "have many forms or faces"
#                Poly = Many    |   Morphe = Form

#                TWO WAYS TO ACHIVE POLYMORPHISM
#                1. Inheritance   = An object can be treated of the same type as a parent class
#                2. "Duck Typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius        

class Square(Shape):
    def __init__(self, side):
        self.side = side
class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base
        
shapes = [Circle(), Square(), Triangle()]   