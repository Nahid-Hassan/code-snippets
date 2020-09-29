#numpy.zeros_like(a, dtype=None, order='K', subok=True)[source]
#Return an array of zeros with the same shape and type as a given array.

import numpy as np
x = np.arange(6)
x = x.reshape(2,3);
print("x = ",x)
print()

#output
#[[0 1 2]
#[3 4 5]]

x = np.zeros_like(x,order='A');
print("x = ",x)
print()
#output: with same shape
#[[0 0 0]
# [0 0 0]]

y = np.arange(3, dtype = float)
print("y = ",y)
print()
#output
#[0. 1. 2.]

y = np.zeros_like(y)
print("y = ",y)
#output
#[0. 0. 0.]