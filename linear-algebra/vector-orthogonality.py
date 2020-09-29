# Two vector are orthogonal if u.v = |u||v|cos@ = 0 or u _|_ v = 90*

import numpy as np

a = np.array([-2, 4, 3])
b = np.array([3, 3, -2])

def is_orthogonal():
    res = np.dot(a, b)
    
    if not res:
        print("Orthogonal")
    else:
        print("not orthogonal")

is_orthogonal()