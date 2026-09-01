# object = A "bundle" of related attributes (variables) and methods (functions)
#          You need a "class" to create object
# class = (blueprint) used to design the structure and layout of an object

# from carClass import Car

class Car:
    def __init__(self, model, year, color, for_sale):     # Constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving a {self.model}.")

    def stop(self):
        print(f"You stopped the {self.model}.")

    def details(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("BMW", 2025, "Black", False)
car2 = Car("Carnival", 2026, "White", True)

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

# car1.drive()
# car1.stop()

car1.details()
car2.details()