#Basic numpy array operation
"""
Created on Sun Mar 17 18:34:13 2019
@author: nahid
"""

import numpy as np

# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]], float)

a = a + 1 #add one all the elements with a 
print(a)
b = b - 1 #subtract 1 all the elements with b
print(b)

c = a * b #scaler multiplication  
print(c)

#matrix multiplication
matrixMultiplication = a.dot(b);
print(matrixMultiplication)

#data types of numpy
print(a.dtype)
print(b.dtype)