"""
Created on Sun Mar 17 18:20:41 2019
@author: nahid
"""
#python program for creating a numpy array
import  numpy as np

#creating a rank 1 array
a = np.array([1,2,3])
print(a, "\n-------------\n")

#creatign a rank 2 array
b = np.array([[1,2,3],
              [4,5,6]]) 
print(b, "\n-------------\n")

#creating a rank 3 array
c = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(c, "\n-------------\n")

#creating a numpy array using tuple
d = np.array((1,2,3))
print(d, "\n-------------\n")