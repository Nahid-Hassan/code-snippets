import pandas as pd
import numpy as np

print(pd.options.display.max_rows) #by default it is 60
pd.options.display.max_rows = 5
print(pd.options.display.max_rows) #Now it is 10

df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
print(df)
'''
     company  numEmps category    ...    state fundedDate raisedAmt
0   LifeLock      NaN      web    ...       AZ   1-May-07   6850000
1   LifeLock      NaN      web    ...       AZ   1-Oct-06   6000000
..       ...      ...      ...    ...      ...        ...       ...
97    MeeVee      NaN      web    ...       CA   1-Feb-06   6500000
98    MeeVee      NaN      web    ...       CA   1-Aug-06   8000000
'''
pd.options.display.max_rows = 100
print(df) #print successfully all the rows in sample.csv data file

#we also can use instead of pd.options.display.max_rows = 5
#*************pd.get_option(arg), set_option(agr,val)*******************

a = pd.get_option("display.max_rows")
print(a) #100
pd.set_option("display.max_rows", 20)
a = pd.get_option("display.max_rows")
print(a) #20

#*******************Example********************************************
df = pd.DataFrame(np.random.randn(10,5))
print(df)
print(df.shape)

pd.set_option("max_rows",5)
print(df)
'''
           0         1         2         3         4
0  -0.957296  0.779242 -1.625559  2.116592 -0.269248
1   0.109035 -0.003971 -0.746726 -1.271288 -0.643878
..       ...       ...       ...       ...       ...
8  -0.550164  0.972242  2.426685  0.408818 -0.136869
9  -0.472941 -0.624765  0.228406 -0.368229  0.101187
'''
#Here we can see 4 line only because the rows evenly spread here

#***************Stretching the DataFrame across pages*****************
df = pd.DataFrame(np.random.randn(5,7))
print(df)
'''
         0         1         2     ...           9         10        11
0  0.017573  0.533890 -1.039920    ...     1.055588  0.230688 -1.185961
1  0.994916  1.730381 -0.265662    ...    -0.637594 -0.468516 -1.197159
2 -0.470152 -0.702236 -0.249671    ...     0.956581 -1.167124 -0.775214
3 -0.113243  0.110624  0.822606    ...     1.375379 -0.564423  0.292864
4 -0.681015 -0.001743  0.170444    ...     0.387591 -0.009591 -0.263648
'''

'''display.expand_frame_repr allows from the representation of dataframes to stretch
   across pages, warpped over the full columns vs row-wise'''
pd.set_option("expand_frame_repr", True)
pd.options.display.expand_frame_repr = 15
print(df)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html
pd.set_option('max_colwidth',6)
dict = {"Name":pd.Series(["Nahid Hassan", "Rafi", "Meem"]),
        "Age":pd.Series([21,22,21]),
        "Weight":pd.Series([48,75,76]),
        "Height":pd.Series([5.3, 5.8, 5.6])}
df = pd.DataFrame(dict)
print(df,"\n")
'''
    Name  Age  Weight  Height
0  Na...   21     48     5.3 
1   Rafi   22     75     5.8 
2   Meem   21     76     5.6  
'''
pd.set_option('max_colwidth',13)
print(df,"\n")
'''
           Name  Age  Weight  Height
0  Nahid Hassan   21      48     5.3
1          Rafi   22      75     5.8
2          Meem   21      76     5.6 
'''
#*****************use reset method********************
pd.reset_option('max_rows')
pd.reset_option('expand_frame_repr')
pd.reset_option('max_colwidth')

pd.set_option('precision',3)
df = pd.DataFrame(np.random.randn(5,4))
print(df)
'''
       0      1      2      3
0 -0.213 -0.518  0.305  0.462
1 -0.812  1.295 -0.891 -1.596
2 -0.511  0.602 -0.174 -0.617
3  0.438 -0.863 -0.318  0.494
4 -0.348  0.584  0.083  0.365
'''

#***********Setting the threshold value below which numbers will be set to zero***********
pd.set_option('chop_threshold',2)
print(df)
'''
     0    1    2    3
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
4  0.0  0.0  0.0  0.0
'''
pd.reset_option('chop_threshold')
print(df)
'''
       0      1      2      3
0  1.195  1.842  0.851 -0.949
1 -1.089 -1.170  1.841 -0.593
2  0.735 -0.322 -1.021 -0.079
3  0.721  1.008  1.689 -0.579
4 -0.858 -0.244  0.758  0.304
'''
