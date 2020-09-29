'''
numpy.where
numpy.where(condition[, x, y])
Return elements chosen from x or y depending on condition.

Parameters:	
condition : array_like, bool
Where True, yield x, otherwise yield y.
'''

import numpy as np
a = np.arange(10)
print(a)

#condition : array_like, bool,Where True, yield x, otherwise yield y.
a = np.where(a == 6, a, a * 5) 
print(a)

#output
'''[ 0  5 10 15 20 25  (condition true for six)6 35 40 45]'''

#This can be used on multidimensional arrays too:
'''don't understand'''
a = np.where([[True, True], [False, False]],
             [[1, 2], [3, 4]],
             [[9, 8], [7, 6]])
print(a,"\n")

#The shapes of x, y, and the condition are broadcast together:
x, y = np.ogrid[:5,:3]

print(np.where(x < y, x, 10 + x))
'''[x, y] = is just like
[[0,0,0,0,...],
 [0,1,1,1....],
 [0,1,2,2....],
 [0,1,2,3....],
 [...........]]
'''

a = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])

print(np.where(a < 4, a, -1))
'''output:
    array([[ 0,  1,  2],
       [ 0,  2, -1],
       [ 0,  3, -1]])
'''