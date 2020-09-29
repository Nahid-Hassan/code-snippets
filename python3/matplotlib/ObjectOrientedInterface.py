# Reference Book: Python Data Science Handbook (page:(222-223))
# Date(14 April, 2019) Day-4

# Importing matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn; seaborn.set() #set plot styles
import pandas as pd 

fig = plt.figure()
x = pd.read_csv('/media/nahid/New Volume/GitHub/Matplotlib/president_heights.csv')
x = np.array(x['height(cm)'])
plt.hist(x,10)

print(plt.show())
fig.savefig('Height Hist Diagram.png')
