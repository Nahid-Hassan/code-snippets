import pandas as pd
import numpy as np

#*****************************From ndarray***************************
#declare 1D, 2D and 3D data
#Series Method converted into all 2D, 3D ... nD data in 1D data
data_1DArray = ['a','v','c','d','m']
data_2DArray = [data_1DArray,[1,2,2,3,4,5,6]];
data_3DArray = [data_2DArray]

ser = pd.Series(data_1DArray)
print(ser,"\n")
'''
output:
0    a
1    v
2    c
3    d
4    m
'''
ser = pd.Series(data_2DArray)
print(ser,"\n")
'''
output:
0          [a, v, c, d, m]
1    [1, 2, 2, 3, 4, 5, 6]
'''
ser = pd.Series(data_3DArray)
print(ser,"\n")
'''
output:
0    [[a, v, c, d, m], [1, 2, 2, 3, 4, 5, 6]]
'''
data_3DArray = [data_2DArray,[data_1DArray]]
ser = pd.Series(data_3DArray) #we also can wirte ser =  pd.Series(data = data_3DArray)
print(ser,"\n")
'''
output:
0    [[a, v, c, d, m], [1, 2, 2, 3, 4, 5, 6]]
1                           [[a, v, c, d, m]]
'''

ser = pd.Series(np.random.randn(5), index=['a','a','c','d','m'])
print(ser,"\n")
'''
output:
a   -1.023070
a   -0.882545
c   -1.326836
d   -1.199390
m    0.113344
'''
print(ser.index)
'''
output:
Index(['a', 'a', 'c', 'd', 'm'], dtype='object')
'''

#*****************************From Dictionary***************************
dict = {'b' : 1, 'a' : 2, 'c' : 3}
ser = pd.Series(data = dict)
print(ser,"\n")
'''
output:
b    1
a    2
c    3
'''
#if an index is passed, the values in data corresponding to the labels int the 
#index will be pulled out
print(ser['b'],"\n")
#output: 1

#Nan value: NaN(Not a Number)is the standerd missing data marker used in pandas.
ser = pd.Series(dict, index=['c','d','a','b'])
print(ser,"\n")
'''
output:
c    3.0
d    NaN #d is not in dict thats why ser['d'] shows NaN value.
a    2.0
b    1.0
'''

#*****************************From Dictionary***************************
#if data is scalar value, an index must be provided, the value will be repeated
#to match the length of index

ser = pd.Series(5.0, index = ['a','b','c'])
print(ser,"\n")
'''
output:
a    5.0
b    5.0
c    5.0
'''
print(pd.Series(50), "\n")
#output: 0 50

#******************************Series is ndarray like********************
ser = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(ser,"\n")
'''
output:
a    0.626603
b    1.839009
c   -0.329370
d   -0.741173
e    0.667815
'''
print(ser[0]," ",ser[1]," ",ser[2],"\n")
#output: -0.4666478378469522   -0.020744654252988565   1.8029439715556583 
#Here we see ser['a'] and ser['0'] is same
print(ser[:3],"\n") #slicing

print(ser[ser>ser.median()],"\n")
#output:c    1.943716, e    1.261358 
#here all the values that greater than ser.median() is showed
print(ser[[1,2,3]],"\n") #inside the 1-D array you passed array index
print(np.exp(ser),"\n")

#**********************Series is also dictionary like********************
#A series is liked a fixed sized dict that you can get and set values by index 
#label:
print(ser['a'],"\n") #-1.3367081098991442 
print('e' in ser,"\n") #Ture
print('f' in ser,"\n") #False
print(ser.get('f'),"\n") # None
print(ser.get('f', np.nan),"\n") #nan(not a number)
print(ser.get('f'),"\n") #None
print('f' in ser,"\n") #False

#************vectorized operations and label alignment with Series******* 
data = [1,2,3,4,5]
ser = pd.Series(data)
print(ser,"\n")
#vectorized operations means we can perform addition, subtraction, multiplications,
#division etc....
ser = ser + ser
print(ser,"\n") #0:2, 1:4, 2:6, 3:8, 4:10
print(ser*0) #all values are zero like 0:0, 1:0, 2:0, 3:0, 4:0

#****************************Name Attribute*****************************
ser = pd.Series(data, name = "Integer type Data")
print(ser,"\n")
print(ser.name,"\n")
