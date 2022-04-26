# If-Else Statement

# Program to print the even numbers
num = int(input("enter the number?"))
if num%2 == 0:
    print("Number is even")
else: print("Number is odd")

# Program to print the largest of the three numbers
a = int(input("Enter a? "));
b = int(input("Enter b? "));
c = int(input("Enter c? "));
if a>b and a>c:
    print("a is largest");
if b>a and b>c:
    print("b is largest");
if c>a and c>b:
    print("c is largest");
else: print("Numbers are equal")

# Nested if Statement
# python program to illustrate nested If statement
# !/usr/bin/python
i = 10
if (i == 10):
    # First if statement
    if (i < 15):
        print("i is smaller than 15")
    # Nested - if statement will only be executed if statement above is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

# if else if ladder (elif statement)
number = int(input("Enter the number?"))
if number==10:
    print("number is equals to 10")
elif number==50:
    print("number is equal to 50");
elif number==100:
    print("number is equal to 100");
else:
    print("number is not equal to 10, 50 or 100")

marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100:
   print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
   print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
   print("You scored grade B ...")
elif marks > 30 and marks <= 40:
   print("You scored grade C ...")
else:
   print("Sorry you are fail ?")