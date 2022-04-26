# for loop

# Iterating over a list
print("List Iteration")
l = ["Ankit", "Gupta"]
for i in l:
	print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("ankit", "gupta")
for i in t:
	print(i)

# Iterating over a String
print("\nString Iteration")
s = "Ankit"
for i in s:
	print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("% s % d" % (i, d[i]))

# for loop Using range() function
# Factorial of number
num = int(input('Number:'))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
	print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1,num + 1):
		factorial = factorial*i
print("The factorial of",num,"is",factorial)

# printing a number
for i in range(10):
	print(i, end=" ")
print()

# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
	print(l[i], end=" ")
print()

# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
	sum = sum + i
print("Sum of first 10 numbers :", sum)

# Program to print table of given number
n = int(input("Enter the number "))
for i in range(1,11):
    c = n*i
    print(n,"*",i,"=",c)

# Program to print even number using step size in range()
n = int(input("Enter the number "))
for i in range(2,n,2):
    print(i)

# Python program to demonstrate for-else loop
for i in range(1, 4):
	print(i)
else: # Executed because no break in for
	print("No Break")
for i in range(1, 4):
	print(i)
	break
else: # Not executed as there is a break
	print("Break")
