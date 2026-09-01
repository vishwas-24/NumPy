# super() = Function used in a child class to call methods from parent class (superclass).
#           Allows you to the extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    
class Square(Shape):
    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side

class Triangle(Shape):
    def __init__(self, color, filled, base, height):
        super().__init__(color, filled)
        self.base = base
        self.height = height

circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, side= 4)
triangle = Triangle(color="yellow", filled=True, base=5, height=7)

print(circle.color)