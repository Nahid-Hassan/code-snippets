#Reference Book: Python Data Science Handbook (page:(33-41))
#Date(11 April, 2019) Day-1

#We’ll start with the standard NumPy import, under the alias np :
import numpy as np

print(np.__version__) #1.16.2


#@@@@@@@@@@@@@@@@@ A Python List Is More Than Just a List @@@@@@@@@@@@@@@@@@@@@
L = list(range(10))

print(L) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[0]) #0
print(L[-1]) #9

print(type(L[0])) #<class 'int'>

L2 = [str(c) for c in L]
print(L2) #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(type(L2[0])) #<class 'str'>

#Because of Python’s dynamic typing, we can even create heterogeneous lists:
L3 = list([True, 'Nahid', 10, 3.14159])
l = [type(item) for item in L3]
print(l) #[<class 'bool'>, <class 'str'>, <class 'int'>, <class 'float'>]
'''
But this flexibility comes at a cost: to allow these flexible types, each item in the list
must contain its own type info, reference count, and other information—that is, each
item is a complete Python object. In the special case that all variables are of the same
type, much of this information is redundant: it can be much more efficient to store
data in a fixed-type array. The difference between a dynamic-type list and a fixed-type
(NumPy-style) array
'''


#@@@@@@@@@@@@@@@@@@@@ Creating Array from Python Lists @@@@@@@@@@@@@@@@@@@@@@@@
#First, we can use np.array to create arrays from Python lists:

npArray = np.array([1,4,2,5,3,6]) #All this data are same type intger type
print(npArray) #[1 4 2 5 3 6]
print(type(npArray)) #<class 'numpy.ndarray'>
print(type(npArray[0])) #<class 'numpy.int64'>

#If types do not match, NumPy will upcast if possible (here, integers are
#upcast to floating point):

npArray = np.array([3.14,4,2,5,3,6])
print(npArray) #[3.14 4.   2.   5.   3.   6.  ] upcast to floating point

#If we want to explicitly set the data type of the resulting array, we can use the dtype
#keyword:

npArray = np.array([3.14,4,2,5,3,6], dtype=np.int64)
print(npArray) #[3 4 2 5 3 6]

#Finally, unlike Python lists, NumPy arrays can explicitly be multidimensional; here’s
#one way of initializing a multidimensional array using a list of lists:

#nested list result in multidimentional array
npArray = np.array([range(i, i + 3) for i in npArray])
print(npArray) #The inner lists are treated as rows of the resulting two-dimensional array.
'''
[[3 4 5]
 [4 5 6]
 [2 3 4]
 [5 6 7]
 [3 4 5]
 [6 7 8]]
'''


#@@@@@@@@@@@@@@@@@@@@@@ Creating Array from Scratch @@@@@@@@@@@@@@@@@@@@@@@@@@@
#Especially for larger arrays, it is more efficient to create arrays from scratch using rou‐
#tines built into NumPy. Here are several examples:

# Create a length-10 integer array filled with zeros
npArray = np.zeros(10, dtype=np.int64)
print(npArray) #[0 0 0 0 0 0 0 0 0 0]

# Create a 3x4 floating-point array filled with 1s
npArray = np.ones((3,4), dtype=np.int64) #by default dtype=float
print(npArray)
'''
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
'''
# Create a 3x4 array filled with 3.14
npArray = np.full((3,4), 3.14159)
print(npArray)
'''
[[3.14159 3.14159 3.14159 3.14159]
 [3.14159 3.14159 3.14159 3.14159]
 [3.14159 3.14159 3.14159 3.14159]]
'''

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
npArray = np.arange(0, 20, 2) #[ 0  2  4  6  8 10 12 14 16 18]
print(npArray)

# Create an array of five values evenly spaced between 0 and 1
# In Deep learning linspace is very much used.
npArray = np.linspace(0,1,5)
print(npArray) #[0.   0.25 0.5  0.75 1.  ]

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
npArray = np.random.random((3,3)) #np.random.random() cannot taken dtpye
print(npArray)
'''
[[0.18791868 0.52966117 0.27389644]
 [0.05022117 0.39274933 0.33032758]
 [0.50074527 0.20817459 0.93269229]]
'''
print(npArray.round(2)) #use round for simplicity
'''
[[0.22 0.73 0.01]
 [0.09 0.39 0.2 ]
 [0.28 0.48 0.98]]
'''

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
npArray = np.random.normal(0, 1, (3,3))
print(npArray)
'''
[[ 0.74609062 -0.77111509  0.73953494]
 [ 1.65073751  0.28092434 -1.34394765]
 [ 0.09287897  1.62158687  0.15536403]]
'''

# Create a 3x3 array of random integers in the interval [0, 10)
npArray = np.random.randint(0,10,(3,3)) #interval[0,10], shape(3,3)
print(npArray)
'''
[[6 5 2]
 [6 2 0]
 [2 5 6]]
'''

# Create a 3x3 identity matrix
npArray = np.eye(3, dtype=np.int16)
print(npArray)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that
# memory location

npArray = np.empty((3,3), dtype=int)
print(npArray)
'''
[[4 5 4]
 [5 4 9]
 [6 1 1]]
'''