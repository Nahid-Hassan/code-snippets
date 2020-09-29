# Reference Book: Python Data Science Handbook (page:(217-222))
# Date(14 April, 2019) Day-4

# Importing matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print(mpl.__version__)  # 3.0.3

# Setting Styles
plt.style.use('seaborn-whitegrid')

x = np.linspace(1, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# print(plt.show())
# plt.savefig('my_figure.png')

# Two Interfaces for the Price of One

#MATLAB-Style Interface 
x = np.linspace(0,10,100)

fig = plt.figure()
plt.subplot(3,1,1) #[rows, columns, panel number]
plt.plot(x, np.sin(x))

plt.subplot(3,1,2)
plt.plot(x, np.cos(x))

plt.subplot(3,1,3)
plt.plot(x, np.tan(x))

print(plt.show())
