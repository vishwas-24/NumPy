# class variables = Shared amonged all instance of class
#                   Defined outside the constructor
#                   Allow you to share data among all object created from that class

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Vishwas", 18)
student2 = Student("STeve", 19)
student3 = Student("Kris", 20)


print("-----------------------")
print(f"Academic Year : {Student.class_year}")
print("-----------------------")
print(f"Total Students : {Student.num_students}")
print("-----------------------")
print(f"Name : {student1.name}")
print(f"Age  : {student1.age}")
print("-----------------------")
print(f"Name : {student2.name}")
print(f"Age  : {student2.age}")
print("-----------------------")
print(f"Name : {student3.name}")
print(f"Age  : {student3.age}")
print("-----------------------")