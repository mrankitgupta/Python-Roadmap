import time

list = dir(time)
print(list)

print(dir(time))

import calendar
print(dir(calendar))

import datetime as dt
print(dir(dt))

import math
print(math.factorial(5))

import random
print(random.randrange(0,10))

from matplotlib import pyplot
pyplot.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20]
           label="BMW", color="blue" width=0.5)
pyplot.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60]
           label="Audi", color= "red", width=0.5)
pyplot.legend()
pyplot.xlabel('days')
pyplot.ylabel('distance (kms)')
pyplot.title('Information')
pyplot.show()

days = [1,2,3,4,5]
sleeping=[7,8,9,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]
slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']

pyplot(slices,
       labels=activities,
       colors=cols,
       startangle=True,
       explode=(0,0.1,0,0),
       autopct'%1.1f%%')

pyplot.title('Pie Plot')
pyplot.show()