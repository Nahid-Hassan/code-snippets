"""
Created on Wed Mar 20 12:06:36 2019
@author: nahid
"""
import numpy as np
#Creating a array using arange() method
a = np.arange(12)
#Shape array with 3 rows and 4 columns
a = a.reshape(3,4)
#'print original array
print(a)


for val in np.nditer(a):
    print(val, end=',')

print('\n----------------------------------------------------\n')
'''The order of iteration is chosen to match the memory layout of an array,
without considering a particular ordering. This can be 
seen by iterating over the transpose of the above array.'''
b = a.T
for val in np.nditer(b):
    print(val, end = ',')

print()
'''
Controlling Iteration Order: 
There are times when it is important to visit the elements 
of an array in a specific order, irrespective of the layout
 of the elements in memory. The nditer object provides an
 order parameter to control this aspect of iteration.
 The default, having the behavior described above, 
 is order=’K’ to keep the existing order. This can be overridden
 with order=’C’ for C order and order=’F’ for Fortran order.
'''
for val in np.nditer(b, order = 'C'):
    print(val, end = ',')

print()

for val in np.nditer(b, order = 'F'):
    print(val, end = ',')
    
'''
Modifying Array Values: 
 The nditer object has another optional parameter called op_flags.
 Its default value is read-only, but can be set to read-write or 
 write-only mode. This will enable modifying array elements using this 
 iterator.
'''
print('\n-----------------------')
for x in np.nditer(a, op_flags = ['readwrite']):
    x[...] = 5*x
print(a)