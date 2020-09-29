# Reference Book: Python Data Science Handbook (page:(51-58))
# Date(12 April, 2019) Day-2, Time = 7:30 PM

import numpy as np
from scipy import special

np.random.seed(0)
# why use numpy??


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


values = np.random.randint(1, 10, size=5)

# print(compute_reciprocals(values))
# 21 ms ± 195 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


# @@@@@@@@@@@@@@@@@@@@@@@@ Introducing UFunc's @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print(1.0/values)
'''
Vectorized operations in NumPy are implemented via ufuncs, whose main purpose is
to quickly execute repeated operations on values in NumPy arrays. Ufuncs are
extremely flexible—before we saw an operation between a scalar and an array, but we
can also operate between two arrays:
'''
a = np.arange(5)  # [0,1,2,3,4]
b = np.arange(1, 6)  # [1,2,3,4,5]
print(a / b)  # [0.         0.5        0.66666667 0.75       0.8       ]

# And ufunc operations are not limited to one-dimensional arrays—they can act on
# multidimensional arrays as well:
a = np.arange(9).reshape(3, 3)
a = 2 ** a
print(a)
'''
[[  1   2   4]
 [  8  16  32]
 [ 64 128 256]]
'''


# @@@@@@@@@@@@@@@@@@@@@@@@ Exploring UFunc's @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Ufuncs exist in two flavors: unary ufuncs, which operate on a single input, and binary
# ufuncs, which operate on two inputs. We’ll see examples of both these types of func‐
# tions here.

# Array Arithmetic
npArray = np.arange(1, 5)  # [1,2,3,4]
print('\nnpArray     =', npArray)
print('npArray + 5 =', npArray + 5)
print('npArray - 5 =', npArray - 5)
print('npArray * 2 =', npArray * 2)
print('npArray / 2 =', npArray / 2)
print('npArray // 5 =', npArray // 2)
print('-npArray =', -npArray)
print('npArray ** 2 =', npArray ** 2)
print('npArray % 5 =', npArray % 2)
'''
npArray     = [1 2 3 4]
npArray + 5 = [6 7 8 9]
npArray - 5 = [-4 -3 -2 -1]
npArray * 2 = [2 4 6 8]
npArray / 2 = [0.5 1.  1.5 2. ]
npArray // 5 = [0 1 1 2]
-npArray = [-1 -2 -3 -4]
npArray ** 2 = [ 1  4  9 16]
npArray % 5 = [1 0 1 0]
'''
# All of these arithmetic operations are simply convenient wrappers around specific
# functions built into NumPy

print('\n', np.add(npArray, 2))  # [3 4 5 6]
print(np.subtract(npArray, 2))  # [-1  0  1  2]
print(np.negative(npArray))  # [-1 -2 -3 -4]
print(np.multiply(npArray, 3))  # [ 3  6  9 12]
print(np.divide(npArray, npArray))  # [1. 1. 1. 1.]
print(np.floor_divide(npArray, 2))  # [0 1 1 2]
print(np.power(npArray, 3))  # [ 1  8 27 64]
print(np.mod(npArray, npArray))  # [0 0 0 0]

# Absolute value
npArray = np.array([-2, -1, 0, 1, 2])
print('\n', npArray)
print(abs(npArray))  # abs is python built in function

# corresponding numpy ufunc is np.absolute()
# which is also available under the np.abs()

print(np.absolute(npArray))  # [2 1 0 1 2]
print(np.abs(npArray))  # [2 1 0 1 2]

# ufunc also handle complex data, in which the absolute value
# returns the magnitude:

npArray = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print('\n', np.abs(npArray))  # [5. 5. 2. 1.]

# Trigonmetric functions
theta = np.linspace(0, np.pi, 3)

print('\n', theta)
print(np.sin(theta))  # [0.0000000e+00 1.0000000e+00 1.2246468e-16]
print(np.cos(theta))  # [ 1.000000e+00  6.123234e-17 -1.000000e+00]
print(np.tan(theta))  # [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]

# Inverse Trigonometric functions are also avaiable:
theta = np.array([-1, 0, 1])

print('\n', np.arcsin(theta))  # [-282.74333882    0.          282.74333882]
print(np.arccos(theta))  # [3.14159265 1.57079633 0.        ]
print(np.arctan(theta))  # [-0.78539816  0.          0.78539816]

#Exponents and logarithms
npArray = np.array([1, 2, 3])

print('\n', npArray)
print(np.exp(npArray))
print(np.exp2(npArray))
print(np.power(3, npArray))

# The inverse of the exponentials, the logarithms, are also available.
npArray = [1, 2, 4, 10]

print('\n', npArray)  # [1, 2, 4, 10]
print(np.log(npArray))  # [0.         0.69314718 1.38629436 2.30258509]
print(np.log2(npArray))  # [0.         1.         2.         3.32192809]
print(np.log10(npArray))  # [0.         0.30103    0.60205999 1.        ]

# There are also some specialized versions that are useful for maintaining precision
# with very small input:

npArray = [0, 0.001, 0.01, 0.1]
print("\nexp(npArray) - 1 =", np.expm1(npArray))
print("log(1 + npArray) =", np.log1p(npArray))
'''
exp(npArray) - 1 = [0.         0.0010005  0.01005017 0.10517092]
log(1 + npArray) = [0.         0.0009995  0.00995033 0.09531018]
'''

# Specialized ufuncs
# NumPy has many more ufuncs available, including hyperbolic trig functions, bitwise
# arithmetic, comparison operators, conversions from radians to degrees, rounding and
# remainders, and much more.
# Another excellent source for more specialized and obscure ufuncs is the submodule
# scipy.special . If you want to compute some obscure mathematical function on
# your data, chances are it is implemented in scipy.special . There are far too many
# functions to list them all, but the following snippet shows a couple that might come
# up in a statistics context:

# Gamma functions (generalized factorials) and related functions
npArray = np.array([1, 5, 10])

print("\ngamma(npArray)      =", special.gamma(npArray))
print("ln|gamma(npArray)| =", special.gammaln(npArray))
print("beta(npArray, 2)      =", special.beta(npArray, 2))
'''
amma(npArray)      = [1.0000e+00 2.4000e+01 3.6288e+05]
ln|gamma(npArray)| = [ 0.          3.17805383 12.80182748]
beta(npArray, 2)      = [0.5        0.03333333 0.00909091]
'''

# Error function (integral of Gaussian)
# its complement, and its inverse

npArray = np.array([0, 0.3, 0.7, 1.0])

print('\nerf(npArray) = ', special.erf(npArray))
print('erfc(npArray) = ', special.erfc(npArray))
print('erfinv(npArray) = ', special.erfinv(npArray))
'''
erf(npArray) =  [0.         0.32862676 0.67780119 0.84270079]
erfc(npArray) =  [1.         0.67137324 0.32219881 0.15729921]
erfinv(npArray) =  [0.         0.27246271 0.73286908        inf]
'''


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ Advanced Ufunc Features @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# specifying output

# For large calculations, it is sometimes useful to be able to specify the array where the
# result of the calculation will be stored. Rather than creating a temporary array, you
# can use this to write computation results directly to the memory location where you’d
# like them to be. For all ufuncs, you can do this using the out argument of the
# function:

x = np.arange(5)
y = np.arange(5)
np.multiply(x, 10, out=y)
print('\n', y)

y = np.zeros(10)
np.power(2, x, out=y[::2])  # x[0,1,2,3,4]
print(y)  # [ 1.  0.  2.  0.  4.  0.  8.  0. 16.  0.]

#Aggregates
x = np.arange(1,6)
print('\n',np.add.reduce(x)) #15
print(np.multiply.reduce(x)) #120

#If we'd like to store all the intermediate results of the compution,
#we can instead use accumulate()
print(np.add.accumulate(x))  # [ 1  3  6 10 15]
print(np.multiply.accumulate(x))  # [  1   2   6  24 120]

#we also use dedicated numpy functions to compute the result
# use np.sum() instead of np.add.reduce()
# use np.prod() instead of np.multiply()
# use np.cumsum() instead of np.add.accumulate()
# use np.cumprod() instead of np.multiply.accumulate()  


#Outer products
x = np.arange(1, 6)
print('\n',np.multiply.outer(x, x))
'''
[[ 1  2  3  4  5]
 [ 2  4  6  8 10]
 [ 3  6  9 12 15]
 [ 4  8 12 16 20]
 [ 5 10 15 20 25]]
'''

#for further readings https://docs.scipy.org/doc/numpy/reference/generated/
