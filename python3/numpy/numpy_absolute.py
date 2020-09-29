"""
Created on Sat Mar 23 00:23:27 2019
@author: nahid
"""
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.absolute.html
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.2, 1.2])
x = np.absolute(x)
print(x)
print(np.absolute(1 + 2j))

#Plot the function over [-10, 10]:
x = np.linspace(-10, 10, 101); #start, end, totalElements you want to create
plt.plot(np.absolute(x))
plt.show()
plt.plot(x)
plt.show()

xx = x + 1j * x[:, np.newaxis]
plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
plt.show()