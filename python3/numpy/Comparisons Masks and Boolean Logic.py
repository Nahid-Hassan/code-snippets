# Reference Book: Python Data Science Handbook (page:(70-77))
# Date(13 April, 2019) Day-3, Time = 3:25 PM

# This section covers the use of Boolean masks to examine and manipulate values
# within NumPy arrays.

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn; seaborn.set() #set plot style

# use Pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('/media/nahid/New Volume/GitHub/Numpy/Seattle2014.csv')['PRCP'].values
# print(rainfall)  

inches = rainfall / 254 #1/10mm -> inches
print(inches.shape) #(365,)

# fig = plt.figure()
# plt.hist(inches, 40)
# print(plt.show())
# fig.savefig('rainfallHistogram.png')

'''
This histogram gives us a general idea of what the data looks like: despite its reputa‐
tion, the vast majority of days in Seattle saw near zero measured rainfall in 2014. But
this doesn’t do a good job of conveying some information we’d like to see: for exam‐
ple, how many rainy days were there in the year? What is the average precipitation on
those rainy days? How many days were there with more than half an inch of rain?
Digging into the data
One approach to this would be to answer these questions by hand: loop through the
data, incrementing a counter each time we see values in some desired range. For rea‐
sons discussed throughout this chapter, such an approach is very inefficient, both
from the standpoint of time writing code and time computing the result. We saw in
“Computation on NumPy Arrays: Universal Functions” on page 50 that NumPy’s
ufuncs can be used in place of loops to do fast element-wise arithmetic operations on
arrays; in the same way, we can use other ufuncs to do element-wise comparisons over
arrays, and we can then manipulate the results to answer the questions we have. We’ll
leave the data aside for right now, and discuss some general tools in NumPy to use
masking to quickly answer these types of questions.
'''

a = np.array([1,2,3,4,5])
print(a < 3)  # [ True  True False False False]
# check this apply all of others relational operator
# like
print(a != 3)  # [ True  True False  True  True]

# It is also possible to do an element-by-element comparison of two arrays, and to
# include compound expressions:

print((2 * a) == (a ** 2))  # [False  True False False False]

'''
As in the case of arithmetic operators, the comparison operators are implemented as
ufuncs in NumPy; for example, when you write x < 3 , internally NumPy uses
np.less(x, 3) . A summary of the comparison operators and their equivalent ufunc
is shown here:

Operator  Equivalent ufunc
==         np.equal
!=         np.not_equal
<          np.less
<=         np.less_equal
>          np.greater
>=         np.greater_equal
'''

# Just as in the case of arithmetic ufuncs, these will work on arrays of any size and
# shape. Here is a two-dimensional example:

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3,4))
print(x)
print(x < 5)
'''
[[5 0 3 3]
 [7 9 3 5]
 [2 4 7 6]]
[[False  True  True  True]
 [False False  True False]
 [ True  True False False]]
'''
print(np.count_nonzero(x < 6)) # 8
print(np.sum(x < 6)) # 8

# how many values less than 6 in each row?
print(np.sum(x < 6, axis=1))  # [4 2 2]

# If we’re interested in quickly checking whether any or all the values are true, we can
# use(you guessed it) np.any() or np.all():

print(np.any(x < 8))  #True
print(np.any(x < 0))  #False
print(np.all(x < 10)) #True
print(np.all(x == 6)) # False

# np.all() and np.any() can be used along particular axes as well. For example:
print(np.all(x < 8, axis=1))  # [ True False  True]

# Here all the elements in the first and third rows are less than 8, while this is not the
# case for the second row.

#Boolean operators
print(np.sum((inches > .5) & (inches < 1)))  # 29
#So we see that there are 29 days with rainfall between 0.5 and 1.0 inches.

#Using the equivalence of A AND B and NOT (A OR B)
print(np.sum(~((inches <= 0.5) | (inches >= 1))))  # 29
'''
The following table summarizes the bitwise Boolean operators and their equivalent
ufuncs:
Operator   Equivalent ufunc
&          np.bitwise_and
|          np.bitwise_or
^          np.bitwise_xor
~          np.bitwise_not
'''
print('Number of days without rain        :',np.sum(inches == 0))
print('Number of days with rain           :',np.sum(inches != 0))
print('Days with more than .5 inches      :',np.sum(inches > 0.5))

'''
Number of days without rain        : 215
Number of days with rain           : 150
Days with more than .5 inches      : 37
'''
print(x[x < 5])  # [0 3 3 3 2 4]
# construct a mask of all rainy days
rainy = (inches > 0)
# construct a mask of all summer days (June 21st is the 172nd day)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
print("Median precip on rainy days in 2014 (inches):", np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ",
      np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
      np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
      np.median(inches[rainy & ~summer]))

#Using the Keywords and/or Versus the Operators &/|
print(bool(42), bool(0)) #True False
print(bool(42 and 0)) #False
print(bool(42 or 0)) #True
print(bin(42))  # 0b101010
print(bin(59))  # 0b111011
print(bin(42 | 59))  # 0b111011

a = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
b = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
print(a | b)  # [ True  True  True False  True  True]
#ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# print( a or b) 

