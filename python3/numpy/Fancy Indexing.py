# Reference Book: Python Data Science Handbook (page:(78-85))
# Date(16 April, 2019) Time = 10:39 PM

import numpy as np 
import pandas as pd

# Exploring Fancy Indexing
rand = np.random.RandomState(42)

a = rand.randint(100,size=10)
print(a)  # [51 92 14 71 60 20 82 86 74 74]

# Suppose we want to access three different elements. We could do it like this:
print([a[9], a[0], a[2]])  # [74, 51, 14]

# Alternatively, we can pass a single list or array of indices to obtain the same result:
idx = [3,4,7]
print(a[idx])  # [71 60 86]

# With fancy indexing, the shape of the result reflects the shape of the index arrays
# rather than the shape of the array being indexed:
idx = np.array([[3,7],
                [4,5]])
print(a[idx])
'''
[[71 86]
 [60 20]]
'''
#Fancy indexing working for multiple dimensions
a = np.arange(12).reshape((3,4))
print(a)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
row = np.array([0,1,2])
col = np.array([2,1,3])

print(a[row, col])  # [ 2  5 11]

# if we combine a column vector and a row vector within the indices, we
# get a two-dimensional result:

#@@@@@@@@@@@@@@@@@ newaxis concept @@@@@@@@@@@@@@@
#https://i.stack.imgur.com/zkMBy.png
'''
In [124]: arr = np.arange(5*5).reshape(5,5)

In [125]: arr.shape
Out[125]: (5, 5)

# promoting 2D array to a 5D array
In [126]: arr_5D = arr[np.newaxis, ..., np.newaxis, np.newaxis]    # arr[None, ..., None, None]

In [127]: arr_5D.shape
Out[127]: (1, 5, 5, 1, 1)
'''

# Don't understand
print(a[row[:,np.newaxis], col])

# Combined Indexing
print(a[2, [2, 0, 1]])  # [10  8  9]
#We also can combine fancy indexing with masking
print(a[1:,[2,0,1]])
'''
[[ 6  4  5]
 [10  8  9]]
'''

