a = 10
b = 5
c = "Ankit"
print(a - b)

print("Ankit")

type("ankit")

a = 50
b = a
print(id(a))
print(id(b))
# Reassigned variable a
a = 500
print(id(a))

name = "A"
Name = "B"
naMe = "C"
NAME = "D"
n_a_m_e = "E"
_name = "F"
name_ = "G"
_name_ = "H"
na56me = "I"
print(name, Name, naMe, NAME, n_a_m_e, NAME, n_a_m_e, _name, name_, _name, na56me)

age = 20
marks = 80.50
print(age)
print(marks)

x = y = z = 50
print(x)
print(y)
print(z)

a, b, c = 5, 10, 15
print(a)
print(b)
print(c)


# Declaring a function
def add():
    # Defining local variables. They has scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)


# Calling a function
add()

add()
# Accessing local variable outside the function
print(a)

# Declare a variable and initialize it
x = 101


# Global variable in function
def mainFunction():
    # printing a global variable
    global x
    print(x)
    # modifying a global variable
    x = 'Welcome To Lenskiller'
    print(x)


mainFunction()
print(x)

# A Python program to display that we can store
# large numbers in Python

a = 10000000000000000000000000000000000000000000
a = a + 1
print(type(a))
print(a)

# Assigning a value to x
x = 6
print(x)
# deleting a variable.
del x
print(x)

a='Hackerearth'
b=[a::-1]

1=[1,2,3,4,5,6,7,8,9]
1=1[::-4]
1=1[-5-5:3]
1=1[0:-1+2]
print(1[-2::]);






