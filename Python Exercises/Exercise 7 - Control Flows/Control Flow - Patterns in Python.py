# Half pyramid pattern

# Using *
n = int(input("Enter the number of rows:"))
# outer loop to handle number of rows
for i in range(0, n):
    # inner loop to handle number of columns
    # values is changing according to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")
        # ending line after each row
    print()

# Using Numbers
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

# Using Characters
n = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(n):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print()

# Inverted Half pyramid pattern

# Using *
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print()

# Using numbers
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Using Characters
n = int(input("Enter number of rows: "))
ascii_value=65
for i in range(n, 0, -1):
    for j in range(1, i+1):
        alphabet=chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value+=1
    print()

# Full Pyramid

# Using *
n = int(input("Enter number of rows: "))
k = 0
for i in range(1, n + 1):
    for space in range(1, (n - i) + 1):
        print(end="  ")
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
    k = 0
    print()

# Using numbers
n = int(input("Enter number of rows: "))
k = 0
count = 0
count1 = 0
for i in range(1, n + 1):
    for space in range(1, (n - i) + 1):
        print("  ", end="")
        count += 1
    while k != ((2 * i) - 1):
        if count <= n - 1:
            print(i + k, end=" ")
            count += 1
        else:
            count1 += 1
            print(i + k - (2 * count1), end=" ")
        k += 1
    count1 = count = k = 0
    print()

# Inverted Full Pyramid
# Generating Inverse Pyramid Pattern Using Stars
n = int(input('Enter number of rows: '))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')  # printing space and staying in same line
    for j in range(2 * i - 1):
        print('*', end='')  # printing * and staying in same line
    print()  # printing new line

# Pascal's Triangle
n = int(input("Enter number of rows: "))
coef = 1
for i in range(1, n+1):
    for space in range(1, n-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

# Floyd's Triangle
n = int(input("Enter number of rows: "))
number = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()