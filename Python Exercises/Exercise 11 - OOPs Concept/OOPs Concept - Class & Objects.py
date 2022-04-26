# Classes & Objects
class car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname, self.year)
c1 = car("BMW", 2022)
c1.display()

# _init_ method
# A Sample class with init method
class Person:
	# init method or constructor
	def __init__(self, name):
		self.name = name
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)
p = Person('Ankit Gupta')
p.say_hi()

# Creating a instance variable of class
# Python3 program to show that the variables with a value assigned in the class declaration, are class variables and
# Variables inside methods and constructors are instance variables.
# Class for Dog
class Dog:
    # Class Variable
    animal = 'dog'
    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

# Delete the object
del Dog

# Counting the Number of objects of a Class
class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1
# creating objects
e1 = Employee()
e2 = Employee()
e2 = Employee()
print("The number of Employee:", Employee.count)


