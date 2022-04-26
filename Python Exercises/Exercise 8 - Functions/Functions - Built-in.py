# abs() Function Example
#  floating number
floating = -20.83
print('Absolute value of -20.83 is:', abs(floating))

# all() Function Example
# all values true
k = [1, 3, 4, 6]
print(all(k))

# all values false
k = [0, False]
print(all(k))

# one false value
k = [1, 3, 7, 0]
print(all(k))

# one true value
k = [0, False, 5]
print(all(k))

# empty iterable
k = []
print(all(k))

# bin() Function Example
x =  10
y =  bin(x)
print (y)

# bool() Function Example
test1 = []
print(test1,'is',bool(test1))
test1 = [0]
print(test1,'is',bool(test1))
test1 = 0.0
print(test1,'is',bool(test1))
test1 = None
print(test1,'is',bool(test1))
test1 = True
print(test1,'is',bool(test1))
test1 = 'Easy string'
print(test1,'is',bool(test1))

# bytes() Function Example
string = "Hello Ankit"
array = bytes(string, 'utf-8')
print(array)

# callable() Function Example
x = 8
print(callable(x))

# compile() Function Example
# compile string source to code
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'sum.py', 'exec')
print(type(code))
exec(code)

# exec() Function Example
x = 8
exec('print(x==8)')
exec('print(x+4)')

# sum() Function Example
s = sum([1, 2, 4])
print(s)
s = sum([1, 2, 4], 10)
print(s)

# any() Function Example
l = [4, 3, 2, 0]
print(any(l))
l = [0, False]
print(any(l))
l = [0, False, 5]
print(any(l))
l = []
print(any(l))

# ascii() Function Example
normalText = 'Python is interesting'
print(ascii(normalText))
otherText = 'Pythön is interesting'
print(ascii(otherText))
print('Pyth\xf6n is interesting')

# bytearray() Function Example
string = "Python is a programming language."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

# eval() Function Example
x = 8
print(eval('x + 1'))

# float() Example
# for integers
print(float(9))
# for floats
print(float(8.19))
# for string floats
print(float("-24.27"))
# for string floats with whitespaces
print(float("     -17.19\n"))
# string float error
# print(float("xyz"))

# format() Function Example
# d, f and b are a type
# integer
print(format(123, "d"))
# float arguments
print(format(123.4567898, "f"))
# binary format
print(format(12, "b"))

# frozenset() Example
# tuple of letters
letters = ('m', 'r', 'o', 't', 's')
fSet = frozenset(letters)
print('Frozen set is:', fSet)
print('Empty frozen set is:', frozenset())

# getattr() Function Example
class Details:
    age = 22
    name = "Phill"
details = Details()
print('The age is:', getattr(details, "age"))
print('The age is:', details.age)

# iter() Function Example
# list of numbers
list = [1, 2, 3, 4, 5]
listIter = iter(list)
# prints '1'
print(next(listIter))
# prints '2'
print(next(listIter))
# prints '3'
print(next(listIter))
# prints '4'
print(next(listIter))

# len() Function Example
strA = 'Python'
print(len(strA))

# list() Example

# locals() Function Example
def localsAbsent():
    return locals()
def localsPresent():
    present = True
    return locals()
print('localsNotPresent:', localsAbsent())
print('localsPresent:', localsPresent())

# map() Function Example
def calculateAddition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(calculateAddition, numbers)
print(result)
# converting map object to set
numbersAddition = set(result)
print(numbersAddition)

# memoryview() Function Example
# A random bytearray
randomByteArray = bytearray('ABC', 'utf-8')
mv = memoryview(randomByteArray)
# access the memory view's zeroth index
print(mv[0])
# It create byte from memory view
print(bytes(mv[0:2]))

#
python = object()

print(type(python))
print(dir(python))

# open() Function Example
# opens python.text file of the current directory
# f = open("python.txt")
# specifying full path
# f = open("E:/Programming/README.txt")

# chr() Function Example
# Calling function
result = chr(102) # It returns string representation of a char
result2 = chr(112)
# Displaying result
print(result)
print(result2)
# Verify, is it string type?
print("is it string type:", type(result) is str)

# Python complex() function example
# Calling function
a = complex(1) # Passing single parameter
b = complex(1,2) # Passing both parameters
# Displaying result
print(a)
print(b)

# delattr() Function Example
class Student:
    id = 101
    name = "Ankit Gupta"
    email = "ankitgupta@abc.com"
# Declaring function
    def getinfo(self):
        print(self.id, self.name, self.email)
s = Student()
s.getinfo()
# delattr(Student,'course') # Removing attribute which is not available
# s.getinfo() # error: throws an error

# dir() Function Example
# Calling function
att = dir()
# Displaying result
print(att)

# Python divmod() function example
# Calling function
result = divmod(10,2)
# Displaying result
print(result)

# dict() function Example
# Calling function
result = dict() # returns an empty dictionary
result2 = dict(a=1,b=2)
# Displaying result
print(result)
print(result2)

# Python filter() function example
def filterdata(x):
    if x>5:
        return x
# Calling function
result = filter(filterdata,(1,2,6))
# Displaying result
# print(list(result))

# hash() Function Example
# Calling function
result = hash(21) # integer value
result2 = hash(22.2) # decimal value
# Displaying result
print(result)
print(result2)

# hash() Function Example
# Calling function
result = hash(21) # integer value
result2 = hash(22.2) # decimal value
# Displaying result
print(result)
print(result2)

# help() Function Example
# Calling function
info = help() # No argument
# Displaying result
print(info)

# min() Function Example
# Calling function
small = min(2225,325,2025) # returns smallest element
small2 = min(1000.25,2025.35,5625.36,10052.50)
# Displaying result
print(small)
print(small2)

# hex() Function Example
# Calling function
result = hex(1)
# integer value
result2 = hex(342)
# Displaying result
print(result)
print(result2)

#
# Calling function
val = id("Ankit Gupta") # string object
val2 = id(1200) # integer object
val3 = id([25,336,95,236,92,3225]) # List object
# Displaying result
print(val)
print(val2)
print(val3)

# setattr() Function Example
class Student:
    id = 0
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name
student = Student(102, "Ankit")
print(student.id)
print(student.name)
# print(student.email) product error
setattr(student, 'email', 'ankit@abc.com')  # adding new attribute
print(student.email)

# sorted() Function Example
str = "Ankit Gupta" # declaring string
# Calling function
sorted1 = sorted(str) # sorting string
# Displaying result
print(sorted1)

# next() Function Example
number = iter([256, 32, 82]) # Creating iterator
# Calling function
item = next(number)
# Displaying result
print(item)
# second item
item = next(number)
print(item)
# third item
item = next(number)
print(item)

# input() Function Example
# Calling function
val = input("Enter a value: ")
# Displaying result
print("You entered:",val)

# int() Function Example
# Calling function
val = int(10) # integer value
val2 = int(10.52) # float value
val3 = int('10') # string value
# Displaying result
print("integer values :",val, val2, val3)

# isinstance() function Example
class Student:
    id = 101
    name = "Ankit"
    def __init__(self, id, name):
        self.id = id
        self.name = name
student = Student(1010, "Ankit")
lst = [12, 34, 5, 6, 767]
# Calling function
print(isinstance(student, Student))  # isinstance of Student class
print(isinstance(lst, Student))

# oct() function Example
# Calling function
val = oct(10)
# Displaying result
print("Octal value of 10:",val)

# ord() function Example
# Code point of an integer
print(ord('8'))
# Code point of an alphabet
print(ord('R'))
# Code point of a character
print(ord('&'))

# pow() function Example
# positive x, positive y (x**y)
print(pow(4, 2))
# negative x, positive y
print(pow(-4, 2))
# positive x, negative y (x**-y)
print(pow(4, -2))
# negative x, negative y
print(pow(-4, -2))

# print() function Example
print("Ankit Gupta")
x = 7
# Two objects passed
print("x =", x)
y = x
# Three objects passed
print('x =', x, '= y')

# range() function Example
# empty range
# print(list(range(0)))
# using the range(stop)
# print(list(range(4)))
# using the range(start, stop)
# print(list(range(1, 7)))

# reversed() function Example
# for string
String = 'Java'
#print(list(reversed(String)))
# for tuple
Tuple = ('J', 'a', 'v', 'a')
#print(list(reversed(Tuple)))
# for range
Range = range(8, 12)
#print(list(reversed(Range)))
# for list
List = [1, 2, 7, 5]
#print(list(reversed(List)))

# round() Function Example
#  for integers
print(round(10))
#  for floating point
print(round(10.8))
#  even choice
print(round(6.6))

# issubclass() Function Example
class Rectangle:
    def __init__(rectangleType):
        print('Rectangle is a ', rectangleType)
class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__('square')
print(issubclass(Square, Rectangle))
print(issubclass(Square, list))
print(issubclass(Square, (list, Rectangle)))
print(issubclass(Rectangle, (list, Rectangle)))

# str() Function Example
str('4')

# tuple() Function Example
t1 = tuple()
print('t1=', t1)
# creating a tuple from a list
t2 = tuple([1, 6, 9])
print('t2=', t2)
# creating a tuple from a string
t1 = tuple('Ankit')
print('t1=', t1)
# creating a tuple from a dictionary
t1 = tuple({4: 'four', 5: 'five'})
print('t1=',t1)

# type() Function Example
List = [4, 5]
print(type(List))
Dict = {4: 'four', 5: 'five'}
print(type(Dict))
class Python:
    a = 0
InstanceOfPython = Python()
print(type(InstanceOfPython))

# vars() Function Example
class Python:
    def __init__(self, x=7, y=9):
        self.x = x
        self.y = y
InstanceOfPython = Python()
print(vars(InstanceOfPython))

# zip() Function Example
numList = [4, 5, 6]
strList = ['four', 'five', 'six']
# No iterables are passed
result = zip()
# Converting itertor to list
resultList = list(result)
print(resultList)
# Two iterables are passed
result = zip(numList, strList)
# Converting itertor to set
resultSet = set(result)
print(resultSet)