# Duck Typing = Another way to achive polymorphiism besides Inheritance
#               Object must have minimum neccessary atributes/methods
#               "If it looks like a duck and quack like a duck, it must be duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)