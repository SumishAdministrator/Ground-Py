"""The Constructor in Python"""
""" When a Object from a Class is created, a method is called automatically (as self) and initialise (using __init__)
the object by setting up its attribute"""

#Ex-1 This Constructor example is without parameters
class Car:
    def __init__(self):

     # Initialise the Car with default attributes   
        self.make = "Jeep"
        self.model = "Meridian"
        self.year = "2023"

#create an instance using the default values
car = Car()
print(car.make)
print(car.model)
print(car.year)


#Ex-2 This Constructor example is with parameters
class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

#create an instance using the parametrised constructor

obj_Flower = Flower("Jasmine", "White")
print(f"The Flower name:",obj_Flower.name)
print(f"The Flower color:",obj_Flower.color)


#Ex-3 This Constructor example is with parameters
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"A new object {self.name} is created with the following age {self.age}")

#Creating an object wgich calls the class MyClass
Object_MyClass = MyClass("Sunil", 22)