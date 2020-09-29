#numpy.zeros(shape, dtype=float, order='C')
#Return a new array of given shape and type, filled with zeros.

import numpy as np

x = np.zeros(5) #by default data type is float
print(x,"\n")

#so

x = np.zeros((5,5), dtype=int) #shape, data type
print(x)
