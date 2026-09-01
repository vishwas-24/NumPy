# Inheritance = Allows a class to inherit attributes and methods from another class 
#               Helps with code reuseability and etensibility
#               Syntax : class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Tommy")
cat = Cat("Cuti")
mouse = Mouse("Mick")

print("-------------------")
print(f"Dog name   : {dog.name}")
print(f"Is alive   : {dog.is_alive}")
dog.eat()
dog.sleep()
print("-------------------")
print(f"Cat name   : {cat.name}")
print(f"Is alive   : {cat.is_alive}")
cat.eat()
cat.sleep()
print("-------------------")
print(f"Mouse name : {mouse.name}")
print(f"Is alive   : {mouse.is_alive}")
mouse.eat()
mouse.sleep()
print("-------------------")