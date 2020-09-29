'''
numpy.vstack(tup)[source]
Stack arrays in sequence vertically (row wise).

This is equivalent to concatenation along the first axis after 1-D arrays 
of shape (N,) have been reshaped to (1,N). Rebuilds arrays divided by vsplit.

This function makes most sense for arrays with up to 3 dimensions. 
For instance, for pixel-data with a height (first axis), width (second axis), 
and r/g/b channels (third axis). The functions concatenate, stack and block 
provide more general stacking and concatenation operations.

Parameters:	
tup : sequence of ndarrays
The arrays must have the same shape along all but the first axis. 
1-D arrays must have the same length.

Returns:	
stacked : ndarray
The array formed by stacking the given arrays, will be at least 2-D.
'''

import numpy as np

x = np.arange(5)
y = np.arange(5,10)

z = np.vstack((x,y))
print(z.ndim)

a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
print(np.vstack((a,b)))
c = np.vstack((a,b))
print(c.shape)