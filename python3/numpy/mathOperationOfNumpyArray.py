#Basic math operation of numpy array
"""
Created on Sun Mar 17 18:39:38 2019
@author: nahid
"""
import numpy as np

# First Array
arr1 = np.array([[4, 7],
                 [2, 6]], 
                 dtype = np.float64)
                  
# Second Array
arr2 = np.array([[3, 6],
                 [2, 8]], 
                 dtype = np.float64) 
 
print(arr1.shape, arr2.shape)

#Addition of two arrays
sumTwoArray = np.add(arr1, arr2) 
print(sum)

#Add all array elements using predefined sum funciton
sum = np.sum(arr1);
print(sum) #19

#square root of array
square_root = np.sqrt((arr1+2+arr2))
print(square_root)

#Transpose of array
#Using in built-in function 'T'
transpose_arr1 = arr1.T
print(transpose_arr1)