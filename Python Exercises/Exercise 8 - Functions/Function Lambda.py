# a is an argument and a+10 is an expression which got evaluated and returned.
x = lambda a:a+10
# Here we are printing the function object
print(x)
print("sum = ",x(20))

# Lambda with User-defined function
def A(x):
    return (lambda y:x+y)
t=A(4)
print(t(8))

# Lambda with filter()
mylist=[1,2,3,4,5,6]
newlist=list(filter(lambda a:(a/3==2),mylist))
print (newlist)

# Lambda with Map()
from functools import reduce
reduce(lambda a,b : a+b, [23,56,43,98,1])

