# Single Inheritance
# Python code to demonstrate how parent constructors are called.
# parent class
class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
# creation of an object variable or an instance
a = Employee('Ankit Gupta', 886012, 200000, "Intern")
# calling a function of the class Person using its instance
a.display()

# Multiple Inheritance
# Python example to show the working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Ankit"
        print("Base1")
class Base2(object):
    def __init__(self):
        self.str2 = "Gupta"
        print("Base2")
class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printStrs(self):
        print(self.str1, self.str2)
ob = Derived()
ob.printStrs()

# Multilevel Inheritance
# A Python program to demonstrate inheritance Base or Super class.
# Note object in bracket. (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is equivalent to "class Person(object)"
class Base(object):
    # Constructor
    def __init__(self, name):
        self.name = name
    # To get name
    def getName(self):
        return self.name
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    # To get name
    def getAge(self):
        return self.age
# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
    # To get address
    def getAddress(self):
        return self.address
# Driver code
g = GrandChild("Ankit", 22, "Pune")
print(g.getName(), g.getAge(), g.getAddress())

# Hierarchical Inheritance
# Python program to demonstrate
# Hierarchical inheritance
# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")
# Derived class1
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")
# Derivied class2
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# Hybrid Inheritance
# Python program to demonstrate
# hybrid inheritance
class School:
	def func1(self):
		print("This function is in school.")
class Student1(School):
	def func2(self):
		print("This function is in student 1. ")
class Student2(School):
	def func3(self):
		print("This function is in student 2.")
class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")
# Driver's code
object = Student3()
object.func1()
object.func2()

# Method Overriding
class Bank:
    def getroi(self):
        return 10;
class SBI(Bank):
    def getroi(self):
        return 7;
class ICICI(Bank):
    def getroi(self):
        return 8;
b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi());
print("SBI Rate of interest:", b2.getroi());
print("ICICI Rate of interest:", b3.getroi());

# Python program to demonstrate private members
# of the parent class
class C(object):
	def __init__(self):
			self.c = 21
			# d is private instance variable
			self.__d = 42
class D(C):
	def __init__(self):
			self.e = 84
			C.__init__(self)
object1 = D()
# produces an error as d is private instance variable
print(object1.d)
