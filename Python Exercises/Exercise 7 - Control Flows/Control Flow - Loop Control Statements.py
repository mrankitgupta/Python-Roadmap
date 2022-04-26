# Break Statement

# Using for loop
str = "Ankit"
for i in str:
    if i == 'k':
        break
    print(i);

# Using while loop
n=2
while 1:
    i=1;
    while i<=4:
        print("%d X %d = %d\n"%(n,i,n*i));
        i = i+1;
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))
    if choice == 0:
        break;
    n=int(input("Enter the number:"))

# Continue Statement

# Using for loop
# loop from 1 to 10
for i in range(1, 11):
    # If i is equals to 6, continue to next iteration without printing
    if i == 6:
        continue
    else:
        # Otherwise print the value of i
        print(i, end=" ")

# Using while loop
# Prints all letters except 't' , 'u' and 'g'
i = 0
a = 'AnkitGupta'
while i < len(a):
    if a[i] == 't' or a[i] == 'u' or a[i] == 'g':
        i += 1
        continue
    print('\nCurrent Letter :', a[i])
    i += 1

# Pass Statement

# Function
def function_name(Ankit):
    pass

#Empty Class
class Ankit:
    pass

# if statement
a = 10
b = 20
if(a<b):
    pass
else:
    print("b<a")

# Using for loop
list =['a', 'b', 'c', 'd']
for i in list:
    if(i =='a'):
        pass
    else:
        print(i)
