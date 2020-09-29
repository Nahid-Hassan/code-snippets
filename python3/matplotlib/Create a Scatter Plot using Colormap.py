# Reference: https://chrisalbon.com/python/basics/set_the_color_of_a_matplotlib/
# Reference: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps

import matplotlib.pyplot as plt
import numpy as np

n = 100
r = 2 * np.random.rand(n)
theta = 2 * np.pi * np.random.rand(n)
area = 200 * r ** 2 * np.random.rand(n)
colors = theta

plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.cool)

print(plt.show())
