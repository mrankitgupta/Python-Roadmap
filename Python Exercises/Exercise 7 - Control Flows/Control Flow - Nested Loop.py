# Nested For Loop

# User input for number of rows
rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0, rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*",end = '')
    print()

# Program to print number pyramid
rows = int(input("Enter the rows"))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end = '')
    print()

# Nested While Loop

# program uses a nested while loop to find the prime numbers from 2 to 20
i = 2
while(i < 20):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1
print ("Good bye!")
