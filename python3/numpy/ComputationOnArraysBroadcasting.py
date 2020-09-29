# Reference Book: Python Data Science Handbook (page:(63-69))
# Date(13 April, 2019) Day-3, Time = 3:25 PM

# Broadcasting is simply a set of rules for applying binary ufuncs(addition,
# subtraction, multiplication, etc.) onarrays of different sizes.

import numpy as np
import matplotlib.pyplot as plt

print('\nIntroducing Broadcasting:')
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

print(a + b)  # [5,6,7]
print(a + 5)  # [5,6,7]

matrix = np.ones((3, 3))
print(matrix + a)
'''
[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]
'''
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a + b)
'''
[[0 1 2]
 [1 2 3]
 [2 3 4]]
'''

# @@@@@@@@@@ Broadcasting example 1 @@@@@@@@@@@@@@@@
print('\nBroadcasting Example -1:')
a = np.ones((2, 3))
b = np.arange(3)

print(a.shape, ' ', b.shape)

'''
We see by rule 1 that the array a has fewer dimensions, so we pad it on the left with
ones:
M.shape -> (2, 3)
a.shape -> (1, 3)
By rule 2, we now see that the first dimension disagrees, so we stretch this dimension
to match:
M.shape -> (2, 3)
a.shape -> (2, 3)
The shapes match, and we see that the final shape will be (2, 3) :
'''
print(a + b)

print('\nBroadcasting example - 2:')
a = np.arange(3).reshape((3, 1))
b = np.arange(3)
# Again, we’ll start by writing out the shape of the arrays:
# a.shape = (3, 1)
# b.shape = (3,)

'''
Rule 1 says we must pad the shape of b with ones:
a.shape -> (3, 1)
b.shape -> (1, 3)
And rule 2 tells us that we upgrade each of these ones to match the corresponding
size of the other array:
a.shape -> (3, 3)
b.shape -> (3, 3)
Because the result matches, these shapes are compatible. We can see this here:
'''

print(a + b)

print('\nBroadcasting example - 3:')
a = np.ones((3,2))
b = np.arange(3)

#print(a + b)
#ValueError: operands could not be broadcast together with shapes (3,2) (3,)

#to bypass this value error we can use np.newaxis method
b = b[:,np.newaxis]

print(a + b)

print('\nBroadcasting in Practice: ')
#Centering an array

a = np.random.random((5,3))
print(a)

aMean = a.mean(0)
print(aMean)

aCentered = a - aMean
print(a)
print(aCentered)
print(aCentered.mean(0))

'''
Broadcasting in Practice: 
[[0.83862929 0.14317788 0.80506902]
 [0.46464661 0.26061009 0.72977281]
 [0.18953245 0.98315161 0.41065711]
 [0.30367627 0.72104366 0.67134196]
 [0.12079467 0.89210426 0.70943855]]

[0.38345586 0.6000175  0.66525589]

[[0.83862929 0.14317788 0.80506902]
 [0.46464661 0.26061009 0.72977281]
 [0.18953245 0.98315161 0.41065711]
 [0.30367627 0.72104366 0.67134196]
 [0.12079467 0.89210426 0.70943855]]

[[ 0.45517343 -0.45683962  0.13981313]
 [ 0.08119075 -0.33940741  0.06451692]
 [-0.19392341  0.38313411 -0.25459878]
 [-0.07977959  0.12102616  0.00608607]
 [-0.26266118  0.29208676  0.04418266]]

[2.22044605e-17 2.22044605e-17 0.00000000e+00]
'''

#Plotting a two-dimensional function
a = np.linspace(0,5,50)
b = np.linspace(0,5,50)[:, np.newaxis]

z = np.sin(a) ** 10 + np.cos(10 + b * a) * np.cos(a)

fig = plt.figure()

plt.imshow(z, origin='lower', extent=[0,5,0,5],cmap='viridis')
plt.colorbar()
fig.savefig('Plotting a two dimensional function')
print(plt.show())