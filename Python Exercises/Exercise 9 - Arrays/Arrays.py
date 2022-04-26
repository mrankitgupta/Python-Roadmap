# Accessing the elements
import array as arr
a = arr.array('i', [2, 4, 6, 8])
print("First element:", a[0])
print("Second element:", a[1])
print("Second last element:", a[-1])

# Add / Change elements in an Array
b = arr.array('i',[1,2,3,4,5,6])
b.append(8)
print("After Append:",b)
b.extend([7,8,9,3])
print("After extend:",b)
b.insert(2,15)
print("After insert:",b)

# Remove / Delete elements in an Array
b.pop()
print("pop1:",b)
b.pop(2)
print("pop2:",b)
b.pop(-1)
print("pop3:",b)
b.remove(8)
print("remove:",b)

# Finding Length of an array
print(len(b))

# Slicing
print (b[0:5])
print(b[0:-2])
print(b[::-1])
print(b)

# Concatenation in Array
c = arr.array('d',[1.1,2.2,3.3,4.5])
d = arr.array('d',[6.1,7.2,3.3,1.1])
e = arr.array('d')
e = c+d
print(e)