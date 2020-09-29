# 6.1 David C. Lay Inner Product

# An inner product is a generalization of the dot product. In a vector space, it is a 
# way to multiply vectors together, with the result of this multiplication being a scalar.

'''
Example: Compute u.v and v.u for u = col(2, -5, -1), v = col(3, 2, -3)

u.v = transpose(u).v = (3 * 2) + (- 5 * 2) + (-1 * -3) = -1
v.u = 10 Because u.v = v.u
'''

u, v = [2, -5, -1], [4, 2, -3]

inner_prod = 0

for i in range(len(u)):
    inner_prod += u[i] * v[i]

print(inner_prod)

# numpy library
import numpy as np

u = np.array([2, -5, -1]);
v = np.array([4, 2, -3]);

inner_prod = np.inner(v, u)

print(inner_prod)

# for 1-d array np.inner(u, v) is same as sum(u[:] * v[:])

inner_prod = sum(u[:] * v[:])
print(inner_prod)

# or  simply

inner_prod = u * v
inner_prod = sum(inner_prod)
print(inner_prod)

x = np.array([[1], [2]])
x_trans = np.transpose(x)
out = np.dot(x_trans, x)

print(sum(out)[0])

# for multi-dimentional array
a = np.array([[1,2], [3,4]]) 
b = np.array([[11, 12], [13, 14]]) 

print(np.inner(a, b))
'''
    In the above case, the inner product is calculated as −
    
    1*11+2*12, 1*13+2*14 
    3*11+4*12, 3*13+4*14 
'''