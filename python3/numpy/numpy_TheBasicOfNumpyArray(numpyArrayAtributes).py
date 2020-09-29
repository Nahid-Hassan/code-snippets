#Reference Book: Python Data Science Handbook (page:(42-50))
#Date(11 April, 2019) Day-1

'''
Data manipulation in Python is nearly synonymous with NumPy array manipulation:
even newer tools like Pandas (Chapter 3) are built around the NumPy array. This sec‐
tion will present several examples using NumPy array manipulation to access data
and subarrays, and to split, reshape, and join the arrays. While the types of operations
shown here may seem a bit dry and pedantic, they comprise the building blocks of
many other examples used throughout the book. Get to know them well!
We’ll cover a few categories of basic array manipulations here:

* Attributes of arrays
  Determining the size, shape, memory consumption, and data types of arrays

* Indexing of arrays
  Getting and setting the value of individual array elements

* Slicing of arrays
  Getting and setting smaller subarrays within a larger array

* Reshaping of arrays
  Changing the shape of a given array

* Joining and splitting of arrays
  Combining multiple arrays into one, and splitting one array into many
'''

#We’ll start with the standard NumPy import, under the alias np :
import numpy as np

print(np.__version__) #1.16.2


#@@@@@@@@@@@@@@@@@@@@@@@@@@ NumPy Array Attributes @@@@@@@@@@@@@@@@@@@@@@@@@@@@
np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size = 5)
x2 = np.random.randint(10, size = (5,5))
x3 = np.random.randint(10,size=(3,4,4))

#Each array has attributes ndim (the number of dimensions), shape (the size of each
#dimension), and size (the total size of the array):

print('Array x1--> Dimension  = ',x1.ndim, ", shape = ", x1.shape, ", size = ",x1.size)
#Array x1--> Dimension  =  1 , shape =  (5,) , size =  5
print('Array x2--> Dimension  = ',x2.ndim, ", shape = ", x2.shape, ", size = ",x2.size)
#Array x2--> Dimension  =  2 , shape =  (5, 5) , size =  25
print('Array x3--> Dimension  = ',x3.ndim, ", shape = ", x3.shape, ", size = ",x3.size)
#Array x3--> Dimension  =  3 , shape =  (3, 4, 4) , size =  48

#some other attributes:
print('Array x3--> dtype  = ',x3.dtype, ", itemsize = ", x3.itemsize, ", nbytes = ",x3.nbytes)
#Array x3--> dtype  =  int64 , itemsize =  8 , nbytes =  384


#@@@@@@@@@@@@@@@@@@ Array Indexing: Accessing Single Elements @@@@@@@@@@@@@@@@@
print(x1) #[5 0 3 3 7]
print('x1[0] = ',x1[0], 'x1[4] = ',x1[4],'x1[-1] = ',x1[-1]) 
#x1[0] =  5 x1[4] =  7 x1[-1] =  7

#In a multidimensional array, you access items using a comma-separated tuple of
#indices
print(x2)
'''
[[9 3 5 2 4]
 [7 6 8 8 1]
 [6 7 7 8 1]
 [5 9 8 9 4]
 [3 0 3 5 0]]
'''
print(x2[0,0]) #9
print(x2[2,0]) #6
print(x2[3, -2]) #9

#You can also modify values using any of the above index notation:

x2[3,-1] = 100.103 #The fraction part should be truncated
print(x2)
'''
[[  9   3   5   2   4]
 [  7   6   8   8   1]
 [  6   7   7   8   1]
 [  5   9   8   9 100]
 [  3   0   3   5   0]]
'''
print(x3)
'''
[[[2 3 8 1]   The output makes you confused but you clear just print(x3[0])
  [3 3 3 7]   print(x3[0]) represent the whole first 2-D array 
  [0 1 9 9]   so,
  [0 4 7 3]]  print(x3[0,1,0]) print--> 3

 [[2 7 2 0]
  [0 4 5 5]   print(x3[1,1,1]) print --> 4
  [6 8 4 1]
  [4 9 8 1]]

 [[1 7 9 9]
  [3 6 7 2]   print(x3[2,2,3]) print --> 9
  [0 3 5 9]
  [4 4 6 4]]]
'''
print(x3[0,1,0]) #3
print(x3[1,1,1]) #4
print(x3[2,2,3]) #9


#@@@@@@@@@@@@@@@@@@@@@@ Array Slicing: Accessing Subarrays @@@@@@@@@@@@@@@@@@@@
#Just as we can use square brackets to access individual array elements, we can also use
#them to access subarrays with the slice notation, marked by the colon ( : ) character.

#variable[start:stop:step] 
#If any of these are unspecified, they default to the values start=0 , stop=size of
#dimension , step=1.

npArray = np.arange(10)
print(npArray) #[0 1 2 3 4 5 6 7 8 9]
 #print first five elements
print(npArray[:5]) #[0 1 2 3 4]
# elements after index 5
print(npArray[5:]) #[5 6 7 8 9]
# middle subarray 
print(npArray[3:7]) #[3 4 5 6]
# Every other element
print(npArray[::2]) #[0 2 4 6 8]
# Every other element, starting at index 1
print(npArray[1::2]) #[1 3 5 7 9]

# A potentially confusing case is when the step value is negative. In this case, the
# defaults for start and stop are swapped. This becomes a convenient way to reverse
# an array:

#all elements, reversed
print(npArray[::-1]) #[9 8 7 6 5 4 3 2 1 0]
print(npArray[5::-2]) #[5,3,1] just like reverse(npArray[0+1:5+1:2])
print(npArray[1:6:2]) #[1 3 5]


#@@@@@@@@@@@@@@@@@@@@@@@@@@ Multidimensional subarrays @@@@@@@@@@@@@@@@@@@@@@@@
npArray = np.random.randint(10, size = (3,4))
print(npArray)
'''
[[4 3 4 4]
 [8 4 3 7]
 [5 5 0 1]]
'''
print(npArray[:2,:3]) #2 rows, 3 columns
'''
[[4 3 4]
 [8 4 3]]
'''
print(npArray[:3,::2]) #3 rows, every other column
'''
[[4 4]
 [8 3]
 [5 0]]
'''
#Finally, subarray dimensions can even be reversed together:
print(npArray[::-1,::-1])
'''
[[1 0 5 5]
 [7 3 4 8]
 [4 4 3 4]]
'''

#@@@@@@@@@@@@@@@@@@@@@@@ Accessing array rows and columns @@@@@@@@@@@@@@@@@@@@@
print(npArray[:, 0]) # [4 8 5] first column of npArray
print(npArray[:,-1]) # [4 7 1] last column of npArray
print(npArray[0 ,:]) # [4 3 4 4] first row of npArray
print(npArray[-1,:]) # [5 5 0 1] last row of npArray


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Subarrays as no-copy views @@@@@@@@@@@@@@@@@@@@@
print(npArray)
'''
[[4 3 4 4]
 [8 4 3 7]
 [5 5 0 1]]
'''
npArray_subArray = npArray[:2,:2]
print(npArray_subArray)
'''
[[4 3]
 [8 4]]
'''
npArray_subArray[0,0] = 99
print(npArray_subArray)
'''
[[99  3]
 [ 8  4]]
'''
print(npArray)
'''
[[99  3  4  4]    !!!!!!!!! 99 is here !!!!!!!!! 
 [ 8  4  3  7]
 [ 5  5  0  1]]
'''
#This default behavior is actually quite useful: it means that when we work with large
#datasets, we can access and process pieces of these datasets without the need to copy
#the underlying data buffer.


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Creating copies of arrays @@@@@@@@@@@@@@@@@@@@@@@
npArray_subArray = npArray[:2,:2].copy()
print(npArray_subArray)
'''
[[4 3]
 [8 4]]
'''
npArray_subArray[0,0] = 10
print(npArray_subArray)
'''
[[10  3]         !!!!!!!!!! 10 is here !!!!!!!!
 [ 8  4]]
'''                      
                            #But
print(npArray)
'''
[[99  3  4  4]    !!!!!!!!! 99 is here !!!!!!!!! 
 [ 8  4  3  7]
 [ 5  5  0  1]]
'''


#@@@@@@@@@@@@@@@@@@@@@@@@@ Reshaping of Arrays @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# The most flexible way of doing this is with the reshape() method
# For example, if you want to put the num‐
# bers 1 through 9 in a 3×3 grid, you can do the following:
ndArray = np.arange(1,10).reshape(3,3) #size(initialArray) = size(reshapedArray)
print(ndArray)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

#newaxis keyword this example used later in this series. as sample
ndArray = np.arange(1,4) #[1 2 3]
ndArray = ndArray[:,np.newaxis]
print(ndArray)
'''
[[1]
 [2]
 [3]]
'''


#@@@@@@@@@@@@@@@@@@@@@@@@ Array Concatenation and Splitting @@@@@@@@@@@@@@@@@@@
# Concatenation, or joining of two arrays in NumPy, is primarily accomplished
# through the routines np.concatenate , np.vstack , and np.hstack . np.concatenate
# takes a tuple or list of arrays as its first argument, as we can see here:

x = np.arange(1,6)
y = np.arange(6,11)

z = np.concatenate([x, y])
print(z) #[ 1  2  3  4  5  6  7  8  9 10]

#You can also concatenate more than two arrays at once:
print(np.concatenate([x,y,z]))
#[ 1  2  3  4  5  6  7  8  9 10  1  2  3  4  5  6  7  8  9 10]

#np.concatenate can also be used for two-dimensional arrays:
grid = np.array([[1,2,3],
                 [4,5,6]])
print(np.concatenate([grid, grid])) # concatenate along the first axis
'''
[[1 2 3]
 [4 5 6]
 [1 2 3]
 [4 5 6]]
'''
print(np.concatenate([grid, grid], axis=1)) # concatenate along the second axis (zero-indexed)
'''
[[1 2 3 1 2 3]
 [4 5 6 4 5 6]]
'''

# or working with arrays of mixed dimensions, it can be clearer to use the np.vstack
# (vertical stack) and np.hstack (horizontal stack) functions:

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b)))
'''
[[1 2 3]
 [4 5 6]]
'''
print(np.hstack((a, b))) #[1 2 3 4 5 6]

a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])

print(np.vstack((a, b)))
'''
[[1]
 [2]
 [3]
 [2]
 [3]
 [4]]
'''
print(np.hstack((a, b)))
'''
[[1 2]
 [2 3]
 [3 4]]
'''
# ----------------------------- Splitting of arrays ---------------------------
# The opposite of concatenation is splitting, which is implemented by the functions
# np.split , np.hsplit , and np.vsplit . For each of these, we can pass a list of indices
# giving the split points:

#np.split(variable,[low, up])
x = [1, 2, 3, 99, 99, 3, 2, 1]

a, b, c = np.split(x, [3,6])
print(a) #[1 2 3]
print(b) #[99 99 3]  #here mid part = x[3,6]
print(c) #[2 1]

a, b, c = np.split(x, [3,5])
print(a) #[1 2 3]
print(b) #[99 99]
print(c) #[3 2 1]

grid = np.arange(1, 17).reshape(4,4)
print(grid)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
'''
upper, lower = np.vsplit(grid,[2])
print(upper)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
print(lower)
'''
[[ 9 10 11 12]
 [13 14 15 16]]
'''
upper, lower = np.vsplit(grid,[3])
print(upper)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(lower)
'''
[[13 14 15 16]]
'''
upper[0,0] = 100
print(grid)
'''
[[100   2   3   4]     !!!!!!!!!!!!! 100 is also here !!!!!!!!!!!!!!!
 [  5   6   7   8]
 [  9  10  11  12]
 [ 13  14  15  16]]
'''
left, right = np.hsplit(grid, [2])
print(left)
'''
[[100   2]
 [  5   6]
 [  9  10]
 [ 13  14]]
'''
print(right)
'''
[[ 3  4]
 [ 7  8]
 [11 12]
 [15 16]]
'''

left, right = np.hsplit(grid, [3])
print(left)
'''
[[100   2   3]
 [  5   6   7]
 [  9  10  11]
 [ 13  14  15]]
'''
print(right)
'''
[[ 4]
 [ 8]
 [12]
 [16]]
'''
#dspilt, dstack, split function is another codefile. maybe named numpy_dspilt_dstack_spilt.py
