# Counter
# A Python program to show different ways to create Counter
import collections
from collections import Counter
# With sequence of items
print(Counter(['B','B','A','B','C','A','B',
			'B','A','C']))
# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
# with keyword arguments
print(Counter(A=3, B=5, C=2))
a= [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
c=collections.Counter(a)
print(c)
print(list(c.elements()))
sub={2:1,6:1}
print(c.subtract(sub))
print(c.most_common())

# Ordered Dict
# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict
print("\nThis is a Dict:")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, value in d.items():
	print(key, value)
print("\nThis is an Ordered Dict:")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print('Before Deleting')
for key, value in od.items():
	print(key, value)
# deleting element
od.pop('a')
# Re-inserting the same
od['a'] = 1
print('\nAfter re-inserting')
for key, value in od.items():
	print(key, value)

# Python program to demonstrate defaultdict
from collections import defaultdict
# Defining the dict
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
# Iterate through the list for keeping the count
for i in L:
	# The default value is 0
	# so there is no need to enter the key first
	d[i] += 1
print(d)
# Defining a dict
d = defaultdict(list)
for i in range(5):
	d[i].append(i)
print("Dictionary with values as list:")
print(d)

#ChainMap
# Python program to demonstrate ChainMap
from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)
# Accessing Values using key name
print(c['a'])
# Accessing values using values() method
print(c.values())
# Accessing keys using keys() method
print(c.keys())
# using new_child() to add new dictionary
d4 = {'g': 7}
c1 = c.new_child(d4)
# printing chainMap
print("Displaying new ChainMap : ")
print(c1)

# Named Tuple
# Python code to demonstrate namedtuple()
from collections import namedtuple
# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
# Adding values
S = Student('Nandini','19','2541997')
# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])
# Access using name
print ("The Student name using keyname is : ",end ="")
print (S.name)
# Adding values
# initializing iterable
li = ['Manjeet', '19', '411997' ]
# initializing dict
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
# using _make() to return namedtuple()
print ("The namedtuple instance using iterable is : ")
print (Student._make(li))
# using _asdict() to return an OrderedDict()
print ("The OrderedDict instance using namedtuple is : ")
print (S._asdict())

# Deque
# Python code to demonstrate deque
from collections import deque
# Declaring deque
queue = deque(['name','age','DOB'])
print(queue)

# Python code to demonstrate working of append(), appendleft()
from collections import deque
# initializing deque
de = deque([1,2,3])
# using append() to insert element at right end, inserts 4 at the end of deque
de.append(4)
# printing modified deque
print ("The deque after appending at right is : ")
print (de)
# using appendleft() to insert element at right end, inserts 6 at the beginning of deque
de.appendleft(6)
# printing modified deque
print ("The deque after appending at left is : ")
print (de)

# Python code to demonstrate working of pop(), and popleft()
# using pop() to delete element from right end, deletes 4 from the right end of deque
de.pop()
# printing modified deque
print ("The deque after deleting from right is : ")
print (de)
# using popleft() to delete element from left end, deletes 6 from the left end of deque
de.popleft()
# printing modified deque
print ("The deque after deleting from left is : ")
print (de)

# UserDict
# Python program to demonstrate userdict
from collections import UserDict
d = {'a':1, 	'b': 2, 	'c': 3}
# Creating an UserDict
userD = UserDict(d)
print(userD.data)
# Creating an empty UserDict
userD = UserDict()
print(userD.data)

# UserList
# Python program to demonstrate userlist
from collections import UserList
L = [1, 2, 3, 4]
# Creating a userlist
userL = UserList(L)
print(userL.data)
# Creating empty userlist
userL = UserList()
print(userL.data)

# UserString
# Python program to demonstrate userstring
from collections import UserString
# Creating a Mutable String
class Mystring(UserString):
	# Function to append to string
	def append(self, s):
		self.data += s
	# Function to remove from string
	def remove(self, s):
		self.data = self.data.replace(s, "")
# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)
# Appending to string
s1.append("s")
print("String After Appending:", s1.data)
# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)