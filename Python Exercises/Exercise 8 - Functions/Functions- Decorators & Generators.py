# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in which the argument is called inner function can access the outer local functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
        # calling the actual function now inside the wrapper function.
        func()
        print("This is after function execution")
    return inner1
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")
# passing 'function_to_be_used' inside the decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)
# calling the function
function_to_be_used()

# find out the execution time of a function using a decorator
# importing libraries
import time
import math
# decorator to calculate duration # taken by any function.
def calculate_time(func):
    # added arguments inside the inner1, if function takes any arguments, can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner1
# this can be added to any function present, in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
# calling the function.
factorial(10)

# Chaining Decorators
# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner
def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner
@decor1
@decor
def num():
	return 10
print(num())


# Decorators with parameters in Python
def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I am", kwargs['name'])
        func()
    # returning inner function
    return inner
@decorator(name="Ankit Gupta")
def my_func():
    print("Inside actual function")

# Generator Function
# A generator function that yields 1 for first time, 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3
# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

# A Python program to demonstrate use of generator object with next()
# A generator function
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3
# x is a generator object
x = simpleGeneratorFun()
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())
