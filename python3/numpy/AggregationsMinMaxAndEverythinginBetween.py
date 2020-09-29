# Reference Book: Python Data Science Handbook (page:(59-))
# Date(13 April, 2019) Day-3

# We’ll start with the standard NumPy import, under the alias np :
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set()  # set plot style

# Often when you are faced with a large amount of data, a first step is to compute sum‐
# mary statistics for the data in question. Perhaps the most common summary statistics
# are the mean and standard deviation, which allow you to summarize the “typical” val‐
# ues in a dataset, but other aggregates are useful as well(the sum, product, median,
# minimum and maximum, quantiles, etc.).

npArray = np.random.random(100)
print('\nSumming the Values in an Array:')
print(round(sum(npArray), 2))  # 52.2
print(np.sum(npArray))  # 52.20359645164018

# big_array = np.random.rand(1000000)
# %timeit sum(big_array) # 10 loops, best of 3: 104 ms per loop
# %timeit np.sum(big_array) # 1000 loops, best of 3: 442 μs per loop

print('\nMinimum and Maximum:')
big_array = np.random.rand(1000000)
print(min(big_array))  # 2.1833396079973255e-07
print(max(big_array))  # 0.9999951829160936

# same function in numpy. numpy version of  the operation is more quickly
print(np.min(big_array))  # 2.1833396079973255e-07
print(np.max(big_array))  # 0.9999951829160936

# For min , max , sum , and several other NumPy aggregates, a shorter syntax is to use
# methods of the array object itself:
print(big_array.min(), big_array.max(), big_array.sum())
# 2.2839487603398823e-06 0.9999994729271785 499748.6111329345

print('\nMultidimensional aggregates:')
matrix_a = np.random.random((3, 4))
print(matrix_a)
'''
[[0.21434649 0.41680862 0.23136847 0.52651149]
 [0.95156885 0.79710065 0.39806083 0.23508013]
 [0.71166791 0.87808004 0.8898395  0.28141989]]
'''
print(matrix_a.sum())  # 4.589765666870639

# Aggregation functions take an additional argument specifying the axis along which
# the aggregate is computed. For example, we can find the minimum value within each
# column by specifying axis = 0:
print(matrix_a.min(axis=0))  # [0.17388545 0.48946081 0.01005003 0.28836908]
print(matrix_a.min(axis=1))  # [0.42009431 0.09302049 0.08362998]

print(matrix_a.max(axis=0))  # [0.74965632 0.93045538 0.84355002 0.81612704]
print(matrix_a.max(axis=1))  # [0.93045538 0.84355002 0.74965632]

'''
Table 2-3. Aggregation functions available in NumPy
Function Name  Nan-safe Version   Description
np.sum         np.nansum          Compute sum of elements
np.prod        np.nanprod         Compute product of elements
np.mean        np.nanmean         Compute median of elements
np.std         np.nanstd          Compute standard deviation
np.var         np.nanvar          Compute variance
np.min         np.nanmin          Find minimum value
np.max         np.nanmax          Find maximum value
np.argmin      np.nanargmin       Find index of minimum value
np.argmax      np.nanargmax       Find index of maximum value
np.median      np.nanmedian       Compute median of elements
np.percentile  np.nanpercentile   Compute rank-based statistics of elements
np.any         N/A                Evaluate whether any elements are true
np.all         N/A Evaluate       whether all elements are true
'''

print('\nExample: What Is the Average Height of US Presidents?:')
data = pd.read_csv(
    '/media/nahid/New Volume/GitHub/Numpy/president_heights.csv')
heights = np.array(data['height(cm)'])
print(pd.DataFrame(data))
'''
    order                    name  height(cm)
0       1       George Washington         189
1       2              John Adams         170
2       3        Thomas Jefferson         189
3       4           James Madison         163
4       5            James Monroe         183
5       6       John Quincy Adams         171
6       7          Andrew Jackson         185
7       8        Martin Van Buren         168
8       9  William Henry Harrison         173
9      10              John Tyler         183
10     11           James K. Polk         173
11     12          Zachary Taylor         173
12     13        Millard Fillmore         175
13     14         Franklin Pierce         178
14     15          James Buchanan         183
15     16         Abraham Lincoln         193
16     17          Andrew Johnson         178
17     18        Ulysses S. Grant         173
18     19     Rutherford B. Hayes         174
19     20       James A. Garfield         183
20     21       Chester A. Arthur         183
21     23       Benjamin Harrison         168
22     25        William McKinley         170
23     26      Theodore Roosevelt         178
24     27     William Howard Taft         182
25     28          Woodrow Wilson         180
26     29       Warren G. Harding         183
27     30         Calvin Coolidge         178
28     31          Herbert Hoover         182
29     32   Franklin D. Roosevelt         188
30     33         Harry S. Truman         175
31     34    Dwight D. Eisenhower         179
32     35         John F. Kennedy         183
33     36       Lyndon B. Johnson         193
34     37           Richard Nixon         182
35     38             Gerald Ford         183
36     39            Jimmy Carter         177
37     40           Ronald Reagan         185
38     41       George H. W. Bush         188
39     42            Bill Clinton         188
40     43          George W. Bush         182
41     44            Barack Obama         185
'''
print(heights)
'''
[189 170 189 163 183 171 185 168 173 183 173 173 175 178 183 193 178 173
 174 183 183 168 170 178 182 180 183 178 182 188 175 179 183 193 182 183
 177 185 188 188 182 185]
'''
print('Mean Heigt:         ', heights.mean())
print('Standerd Deviation: ', heights.std())
print('Maximum Height:     ', heights.min())
print('Minimum Height:     ', heights.max())
'''
Mean Heigt:          179.73809523809524
Standerd Deviation:  6.931843442745892
Maximum Height:      163
Minimum Height:      193
'''
print("25th Percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th Percentile:   ", np.percentile(heights, 75))
'''
25th Percentile:    174.25
Median:             182.0
75th Percentile:    183.0
'''
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('Height(cm)')
plt.ylabel('Number')

print(plt.show())

'''
These aggregates are some of the fundamental pieces of exploratory data analysis that
we’ll explore in more depth in later chapters of the book.
'''

# https://matplotlib.org/users/pyplot_tutorial.html
# https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/data/president_heights.csv
