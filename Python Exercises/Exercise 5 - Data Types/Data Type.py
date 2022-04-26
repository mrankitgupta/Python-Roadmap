# Number
a=5
print(a)
print(type(a))
b=40.5
print(b)
print(type(b))
c=1+3j
print(c)
print(type(c))

# Sequence Type

# String
str1='hello ankit' #string str1
str2='how are you?' #string str2
print(str1[0:3]) #printing first 3 character using slice operator
print(str1[4]) #printing 4th charachter of the string
print(str1*2) #printing the string twice
print(str1+str2) #printing the concatenation of str 1 and str 2
print(str1.upper())

#List
list1 = [1, "hi", "Python", 2]
# Checking type of given list
print(type(list1))

# Printing the list1
print(list1)
# List slicing
print(list1[3:])
# List slicing
print(list1[0:2])
# List Concatenation using + operator
print(list1 + list1)
# List repetation using * operator
print(list1 * 3)
print(list1[2])
list1[3]=5
print(list1[3])
list1.append(8)
print(list1)
list1.insert(3,50)
print(list1)
list1.reverse()
print(list1)

#Tuple
tup = ("hi", "Python", 2)
# Checking type of tup
print(type(tup))
# Printing the tuple
print(tup)
# Tuple slicing
print(tup[1:])
print(tup[0:1])
# Tuple concatenation using + operator
print(tup + tup)
# Tuple repatation using * operator
print(tup * 3)
print(tup.count('Python'))
print(tup[0])

#Dictionary
d = {1: 'Ankit', 2: 'Alex', 3: 'john', 4: 'mike', 'third': 'Any'}
# Printing dictionary
print(d)
# Accesing value using keys
print("1st name is " + d[1])
print("2nd name is " + d[4])
print(d.keys())
print(d.values())
print(d['third'])
print(d.get(3))
d['third']='Gupta'
print(d)
d[5]='Jimmy'
print(d)

#Set
# Creating Empty set
set1 = set()
set2 = {'Ankit', 2, 3,2, 'Python'}
# Printing Set value
print(set2)
# Adding element to the set
set2.add(10)
print(set2)
# Removing element from the set
set2.remove(2)
print(set2)

#Boolean
print(type(True))
print(type(False))
num=9>8
print(type(num))
print(num)

#Type Conversion
#Implicit type conversion
x = 10
print("x is of type:",type(x))
y = 10.6
print("y is of type:",type(y))
x = x + y
print(x)
print("x is of type:",type(x))

#Explicit type conversion
# using int(), float()
# initializing string
s = "10010"
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)

# using tuple(), set(), list()
# initializing string
s = 'ankit'
# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c)
# printing string converting to set
c = set(s)
print ("After converting string to set : ",end="")
print (c)
# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c)

# using dict(), complex(), str()
# initializing integers
a = 1
b = 2
# initializing tuple
tup = (('a', 1) ,('f', 2), ('g', 3))
# printing integer converting to complex number
c = complex(1,2)
print ("After converting integer to complex number : ",end="")
print (c)
# printing integer converting to string
c = str(a)
print ("After converting integer to string : ",end="")
print (c)
# printing tuple converting to expression dictionary
c = dict(tup)
print ("After converting tuple to dictionary : ",end="")
print (c)

# using ord(), hex(), oct()
# initializing integer
s = '4'
# printing character converting to integer
c = ord(s)
print ("After converting character to integer : ",end="")
print (c)
# printing integer converting to hexadecimal string
c = hex(56)
print ("After converting 56 to hexadecimal string : ",end="")
print (c)
# printing integer converting to octal string
c = oct(56)
print ("After converting 56 to octal string : ",end="")
print (c)

# Convert ASCII value to characters
a = chr(76)
b = chr(77)
print(a)
print(b)

print("\a")