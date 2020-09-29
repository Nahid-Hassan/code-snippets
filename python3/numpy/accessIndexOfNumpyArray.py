#accssing the numpy array index
"""
Created on Sun Mar 17 18:28:11 2019
@author: nahid
"""
import numpy as np

#creating a rank 4 array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

#printing a range of array with using slicing method
sliced_arr = arr[:3, ::3]
print(sliced_arr)

#printing elements using specific index
index_arr = arr[1,1] #access just one element
print(index_arr)

index_arr = arr[[1,0,3,2], #access (1,2), (0,3), (3,1) & (2,0) index
                [2,3,1,0]]
print(index_arr)
