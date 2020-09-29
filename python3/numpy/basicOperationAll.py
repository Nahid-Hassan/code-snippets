"""
Created on Sun Mar 17 20:01:22 2019
@author: nahid
"""
import numpy as np
 
a = np.array([1, 2, 5, 3])
 
# add 1 to every element
print ("Adding 1 to every element:", a+1)
 
# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3)
 
# multiply each element by 10
print ("Multiplying each element by 10:", a*10)
 
# square each element
print ("Squaring each element:", a**2)
 
# modify existing array
a *= 2
print ("Doubled each element of original array:", a)
 
# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
 
print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)


#------------------------------------------------------------
#maximum element of the array
print('Largest element is:', a.max())

#print raw and coloum based maximum and minmum element 
#for raw using axis = 1 and for coloum = 0
print ("Row-wise maximum, minimum elements:", 
                    a.max(axis = 1), a.min(axis = 1))
 
print ("Column-wise maximum, minimum elements:",
                        a.max(axis = 0), a.min(axis = 0))

#sum of array elements
print('Sum of array elements = ', a.sum())

#cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        a.cumsum(axis = 1))

#----------------------------------------------------------
# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))
 
# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))
 
# square root of array values
print ("Square root of array elements:", np.sqrt(a))

