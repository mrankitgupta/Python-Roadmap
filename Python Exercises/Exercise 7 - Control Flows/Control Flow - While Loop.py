# While Loop
count = 0
while (count < 3):
	count = count + 1
	print("Hello Ankit")

# checks if list still contains any element
a = [1, 2, 3, 4]
while a:
	print(a.pop())

# Program to print table of given numbers
i=1
number=0
b=9
number = int(input("Enter the number:"))
while i<=10:
    print("%d X %d = %d" %(number,i,number*i))
    i = i+1

# Using else with while loop
i=int(input("Enter the number:"))
while(i<=5):
    print(i)
    i=i+1
else:
    print("The while loop exhausted")

# Using else with while loop
# Program to print Fibonacci numbers to given limit
terms = int(input("Enter the terms "))
# first two initial terms
a = 0
b = 1
count = 0
# check if the number of terms is Zero or negative
if (terms <= 0):
	print("Please enter a valid integer")
# if there is only one term, return a
elif (terms == 1):
	print("Fibonacci sequence upto", limit, ":")
	print(a)
# generate fibonacci sequence
else:
	print("Fibonacci sequence:")
	while (count < terms):
		print(a, end=' ')
		c = a + b
		# updating values
		a = b
		b = c
		count += 1

# Sentinel controlled statement
a = int(input('\nEnter a number (-1 to quit): '))
while a != -1:
	a = int(input('Enter a number (-1 to quit): '))

# Do-While Loop
i = 1
while True:
	print(i)
	i = i + 1
	if (i > 5):
		break

# Infinite While Loop
var = 1
while(var != 2):
    i = int(input("Enter the number:"))
    print("Entered value is %d"%(i))
