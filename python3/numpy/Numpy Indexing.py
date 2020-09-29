"""
Created on Tue Mar 19 12:03:09 2019
@author: nahid
"""
import numpy as np

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l1 * l2) #TypeError: can't multiply sequence by non-int of type 'list'

# But....We can easily be done with NumPy arrays.
a1, a2 = np.array(l1), np.array(l2)
print(a1 * a2)  # [  1   4   9  16  25  36  49  64  81 100]

# ------------------------------------------------------------------------------
# Python program to demonstrate the use of index arrays
# Creating a sequence of integers from 10 to 1 with a step of -2

a = np.arange(10, 1, -2)
print(a)
print()

newA = a[np.array([3, 2, 1, -1])]
print(newA)

# ------------------------------------------------------------------------------
# Python program for basic slicing.
# Arrange elements from 0 to 19
a = np.arange(20)
print("\n Array is:\n ", a)

# a[start:stop:step] start = index, stop = value where stop step = ++ / --
print("\n a[-8:17:1]  = ", a[-5:17:1])

# The : operator means all elements till the end.
print("\n a[10:]  = ", a[10:])
print()

# ------------------------------------------------------------------------------
a = np.array([[0, 1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10, 11],
              [12, 13, 14, 15, 16, 17],
              [18, 19, 20, 21, 22, 23],
              [24, 25, 26, 27, 28, 29],
              [30, 31, 32, 33, 34, 35]])
print(a.ndim)
# slicing and indexing
print("\n a[0, 3:5]  = ", a[0, 3:5])

print("\n a[4:, 4:]  = ", a[4:, 4:])

print("\n a[:, 2]  = ", a[:, 2])

# এখনো বুঝি নাই। @@@@@@@@@@@@@
print("\n a[2::2, ::2]  = ", a[2::2, ::2])

# A 3 dimensional array.
b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]])

print(b[..., 1])  # Equivalent to b[: ,: ,1 ]
print(b.ndim)

# ------------------------------------------------------------------------------
# Python program showing advanced indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 0, 1]])

# Python program showing advanced
# and basic indexing
a = np.array([[0, 1, 2], [3, 4, 5],
              [6, 7, 8], [9, 10, 11]])

print(a.shape)
print(a[1:2, 1:3])
print(a[1:2, [1, 2]])

# You may wish to select numbers greater than 50
a = np.array([10, 40, 80, 50, 100])
print(a[a > 50])
