#Reference Book Matplotlib

import matplotlib.pyplot as plt 
import numpy as np 

#plt.style.use('seaborn-whitegrid')

x = np.linspace(0,2,100)

plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='Quadratic')
plt.plot(x, x ** 3, label='Cubic')

plt.xlabel('X level')
plt.ylabel('Y level')

plt.title('Linear, Quadratic and Cubic line')

plt.legend()

print(plt.show())


'''
	The first call to plt.plot will automatically create the necessary figure and axes to achieve
	the desired plot. Subsequent calls to plt.plot re-use the current axes and each add another
	line. Setting the title, legend, and axis labels also automatically use the current axes and set
	the title, create the legend, and label the axis respectively.
	pylab is a convenience module that bulk imports matplotlib.pyplot (for plotting) and numpy
	(for mathematics and working with arrays) in a single name space. pylab is deprecated and
	its use is strongly discouraged because of namespace pollution. Use pyplot instead.
	For non-interactive plotting it is suggested to use pyplot to create the figures and then the
	OO interface for plotting.
'''
