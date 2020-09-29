import pandas as pd

#************************Creating DataFrames*************************
fruits = {'a':'apple','b':'ball', 'c': 'cat'}
fruits = pd.DataFrame(fruits, index=[1,2,3]) #this fruits name is used pd.Panel()
print(fruits,"\n")
'''
output:
       a     b    c
1  apple  ball  cat
2  apple  ball  cat
3  apple  ball  cat
'''
persons = {'a':'anik','b':'bibek', 'c': 'choity', 'd':'dolly'}
persons = pd.DataFrame(persons, index=[1,2,3,4]) #this fruits name is used pd.Panel()
print(persons,"\n")
'''
output:
      a      b       c
1  anik  bibek  choity
2  anik  bibek  choity
3  anik  bibek  choity
'''
#*********************Creating Panel*******************************
pan = pd.Panel(data={'Item1':fruits, 'Item2':persons},items=['Item1','Item2'],
               major_axis=[1,2,3], minor_axis=['a','b','c','d'])
print(pan,"\n")
'''
output:
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 3 (major_axis) x 4 (minor_axis)
Items axis: Items1 to Item2
Major_axis axis: 1 to 3
Minor_axis axis: a to d 
'''
#********************Getting individual Items***********************
print(pan['Item1'],"\n")
'''
output:
       a     b    c    d
1  apple  ball  cat  NaN
2  apple  ball  cat  NaN
3  apple  ball  cat  NaN
'''
print(pan['Item2'],"\n")
'''
output:
      a      b       c      d
1  anik  bibek  choity  dolly
2  anik  bibek  choity  dolly
3  anik  bibek  choity  dolly
'''
#**********************Getting Axes names***************************
print(pan.axes,"\n")
'''
output:
[Index(['Item1', 'Item2'], dtype='object'), Int64Index([1, 2, 3], dtype='int64'), Index(['a', 'b', 'c', 'd'], dtype='object')]
'''
#**********************Getting items names***************************
print(pan.items,"\n")
#output: Index(['Item1', 'Item2'], dtype='object') 
#**************Getting major_axis minor_axis & dimension*************
print(pan.major_axis,"\n") #Int64Index([1, 2, 3], dtype='int64')
print(pan.minor_axis,"\n") #Index(['a', 'b', 'c', 'd'], dtype='object')
print(pan.ndim,"\n") #3

#**************Getting dtypes, shape, size, values*****************
print(pan.dtypes,"\n") #object type
print(pan.shape,"\n") #(2,3,4)
print(pan.size,"\n") #24
print(pan.values,"\n") 
'''
output:
[[['apple' 'ball' 'cat' nan]
  ['apple' 'ball' 'cat' nan]
  ['apple' 'ball' 'cat' nan]]

 [['anik' 'bibek' 'choity' 'dolly']
  ['anik' 'bibek' 'choity' 'dolly']
  ['anik' 'bibek' 'choity' 'dolly']]] 
'''

#**********************Passing 3-Dimensional Array**********************
#Example-1
data = [[[1,2,3,4,5]]]
pan = pd.Panel(data=data, items=['Item1'])
print(pan, "\n")
'''
Output:
<class 'pandas.core.panel.Panel'>
Dimensions: 1 (items) x 1 (major_axis) x 5 (minor_axis)
Items axis: Item1 to Item1
Major_axis axis: 0 to 0
Minor_axis axis: 0 to 4
'''
print(pan['Item1'],"\n")
'''
output:
   0  1  2  3  4
0  1  2  3  4  5
'''
#Example-2
data=[[[1,2,3,4,5,6]]]
pan = pd.Panel(data=data, items=['Item1'], major_axis=['Row1'],
               minor_axis=['a','b','c','d','e','f'])
print(pan,"\n")
'''
output:
<class 'pandas.core.panel.Panel'>
Dimensions: 1 (items) x 1 (major_axis) x 6 (minor_axis)
Items axis: Item1 to Item1
Major_axis axis: Row1 to Row1
Minor_axis axis: a to f 
'''
print(pan['Item1'],"\n")
'''
output:
      a  b  c  d  e  f
Row1  1  2  3  4  5  6 
'''
data=[[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]]
pan = pd.Panel(data=data, items=['Item1'], major_axis=['Row1','Row2','Row3'],
               minor_axis=['a','b','c','d','e','f'])
print(pan,"\n")
'''
output:
<class 'pandas.core.panel.Panel'>
Dimensions: 1 (items) x 3 (major_axis) x 6 (minor_axis)
Items axis: Item1 to Item1
Major_axis axis: Row1 to Row3
Minor_axis axis: a to f
'''
print(pan['Item1'])
'''
Output:
       a   b   c   d   e   f
Row1   1   2   3   4   5   6
Row2   7   8   9  10  11  12
Row3  13  14  15  16  17  18
'''
