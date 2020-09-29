#Reference Book Matplotlib 
#Chapter Tutorial  

import matplotlib.pyplot as plt

fig = plt.figure() # an empty figure with no axes
fig.suptitle('No axes on this figure') # add an title so we know which is this
        
print(plt.show()) # this line of code show the figure on the windows
fig.savefig('Create a simple figure.png') # save the figure 