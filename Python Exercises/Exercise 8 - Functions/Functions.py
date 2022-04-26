# Function Calling
# function definition
def hello_world():
    print("Hello Ankit")
# function calling
hello_world()

# Return statement
# Defining function
def sum():
    a = 10
    b = 20
    c = a+b
    return c
# calling sum() function in print statement
print("The sum is:",sum())

# Creating function without return statement
# Defining function
def sum():
    a = 10
    b = 20
    c = a+b
# calling sum() function in print statement
print(sum())

# Arguments in Function
# defining the function
def func (name):
    print("Hi ",name)
#calling the function
func ("Ankit")

# Python function to calculate the sum of two variables
# defining the function
def sum(a, b):
    return a + b;
# taking values from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
# printing the sum of a and b
print("Sum = ", sum(a, b))

# Call by reference in Python
# Ex.- Passing Immutable Object (List)
# defining the function
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function = ", list1)
# defining the list
list1 = [10, 30, 40, 50]
# calling the function
change_list(list1)
print("list outside function = ", list1)

# Ex - Passing Mutable Object (String)
# defining the function
def change_string(str):
    str = str + " Hows you "
    print("printing the string inside function :", str)
strin = "Hi I am there"
# calling the function
change_string(strin)
print("printing the string outside function :", strin)

# Arguments
# Required Arguments
def func(name):
    message = "Hi "+name
    return message
Name = input("Enter the name:")
print(func(Name))

#the function simple_interest accepts three arguments and returns the simple interest accordingly
def simple_interest(p,t,r):
    return (p*t*r)/100
P = float(input("Enter the principle amount? "))
T = float(input("Enter the time in years? "))
R = float(input("Enter the rate of interest? "))
print("Simple Interest: ",simple_interest(P,T,R))

# Default Arguments
def printme(name,age=22):
    print("My name is",name,"and age is",age)
printme(name = "Ankit")

def printme(name,age=22):
    print("My name is",name,"and age is",age)
printme(name = "Ankit")
#the variable age is not passed into the function however the default value of age is considered in the function
printme(age = 10,name="Mr Ankit Gupta")
#the value of age is overwritten here, 10 will be printed as age

# Variable-length Arguments (*args)
def printme(*names):
    print("type of passed argument is ",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)
printme("Ankit","Gupta","smith","nick")

# Keyword arguments(**kwargs)
# providing the values in different order at the calling
#The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case
def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))

# Many arguments using Keyword argument
def food(**kwargs):
    print(kwargs)
food(a="Apple")
food(fruits="Orange", Vegetables="Carrot")

# Scope of variables
# Global Variable
def calculate(*args):
    sum=0
    for arg in args:
        sum = sum +arg
    print("The sum is",sum)
sum=0
calculate(10,20,30) #60 will be printed as the sum
print("Value of sum outside the function:",sum) # 0 will be printed  Output:

# Local Variable
def print_message():
    message = "hello !! I am going to print a message." # the variable message is local to the function itself
    print(message)
print_message()
print(message) # this will cause an error since a local variable cannot be accessible here