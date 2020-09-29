import pandas as pd
import numpy as np

#***********************From dict of Series or dicts********************
#dictionary takes key:value
dict = {"Name":pd.Series(["Nahid", "Rafi", "Meem"]),
        "Age":pd.Series([21,22,21]),
        "Weight":pd.Series([48,75,76]),
        "Height":pd.Series([5.3, 5.8, 5.6])}
df = pd.DataFrame(dict)
print(df,"\n")
'''
Output:
0  Nahid   21      48     5.3
1   Rafi   22      75     5.8
2   Meem   21      76     5.6 
'''
df = pd.DataFrame(dict, index=[1]) #1  Rafi   22      75     5.8
print(df,"\n") #1  Rafi   22      75     5.8
'''
output:
   Name  Age  Weight  Height
1  Rafi   22      75     5.8
'''
#with use index
dict1 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
      'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(dict1)
print(df,"\n")
'''
output:
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0
'''
print(pd.DataFrame(dict1, index=['b', 'a', 'd']),"\n")
'''
output:
   one  two
b  2.0  2.0
a  1.0  1.0
d  NaN  4.0
'''
#The row and column labels can be accessed respectively 
#by accessing the index and columns attributes:

#Note When a particular set of columns is passed along with a dict of data,
#the passed columns override the keys in the dict.
print(pd.DataFrame(dict1, index=['d','b','a'], columns=['two','three']),"\n")
'''
output:
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN
'''
#***********getting index name and column name of a dataFrame obj**********
print(df.columns) #Index(['one', 'two'], dtype='object')
print(df.index,"\n") #Index(['a', 'b', 'c', 'd'], dtype='object') 

#we can passed a list
dict = {"Name":["Nahid", "Rafi", "Meem"],
        "Age":[21,22,21],
        "Weight":[48,75,76],
        "Height":[5.3, 5.8, 5.6]}
df = pd.DataFrame(dict)
print(df,"\n")
'''
Output:
0  Nahid   21      48     5.3
1   Rafi   22      75     5.8
2   Meem   21      76     5.6 
'''
print(df.index) #RangeIndex(start=0, stop=3, step=1)
print(df.columns) #Index(['Name', 'Age', 'Weight', 'Height'], dtype='object')

#************Create DataFrame a list of dictionaries**************
data = [{'c':0, 'b':3},{'a':10, 'c':30, 'b':7}]
df = pd.DataFrame(data)
print("\n",df)
'''
output:
    a  b   c
0   NaN  3   0
1  10.0  7  30
'''
df = pd.DataFrame(data, index=["first", "second"])
print("\n",df,"\n")
'''
output:
            a  b   c
first    NaN  3   0
second  10.0  7  30 
'''
 
df = pd.DataFrame(data, columns=['A', 'b', 'C']) #must same as data key
print(df,"\n")
'''
    A  b   C
0 NaN  3 NaN
1 NaN  7 NaN
'''


#**********columns selection, addition, deletion method*****************
dict = {"Name":["Nahid", "Rafi", "Meem", "Himu", "Minhaz"],
        "Age":[21,22,21,21,23],
        "Weight":[48,75,76,55,86],
        "Height":[5.3, 5.8, 5.6,5.0,5.8]}
df = pd.DataFrame(dict)
print(df,"\n")
print(df['Name'],"\n") #also try df['Age'], df['Weight'], df['Height']
'''
output:
0     Nahid
1      Rafi
2      Meem
3      Himu
4    Minhaz
'''

#*******************Calculating BMI For all Members*********************
#Insert Method
'''DataFrameName.insert(loc, column, value, allow_duplicates = False)'''

slen = len(df['Name'])
df.insert(4, 'BMI', round((df['Weight'] / ((df['Height'] * .3048)**2)),2), True)
print(df)
'''
output:
     Name  Age  Weight  Height    BMI
0   Nahid   21      48     5.3  18.39
1    Rafi   22      75     5.8  24.00
2    Meem   21      76     5.6  26.09
3    Himu   21      55     5.0  23.68
4  Minhaz   23      86     5.8  27.52
'''

#***********columns canbe deleted or popped like with a dict*********
#first we insert a temporary column and then it delete or pop
df.insert(5, "CGPA", [3.97,4.0,3.98,3.99,4.00], True) #loc is start from 0
print("\n",df)
'''
output:
      Name  Age  Weight  Height    BMI  CGPA
0   Nahid   21      48     5.3  18.39  3.97
1    Rafi   22      75     5.8  24.00  4.00
2    Meem   21      76     5.6  26.09  3.98
3    Himu   21      55     5.0  23.68  3.99
4  Minhaz   23      86     5.8  27.52  4.00
'''
del(df['CGPA']) #Instead of del you also can used df.pop('CGPA')
print("\n",df)
#insert new column
df['New'] = [1,2,3,4,5] #you can also write df['New'] = 10 but you can't
#df['New'] = [1,2,3,4,5,6] .... out of range
print("\n",df)
df.pop('New')
print("\n",df)
 #******************also u can use assign method*******************
df = df.assign(assign_col=lambda x: x.Weight * 9 / 5 + 32)
print("\n",df)
df = pd.DataFrame({'temp_c': [17.0, 25.0]},
                   index=['Portland', 'Berkeley'])
print("\n",df)
df = df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
print("\n",df) 
#http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html

#Alternatively, the same behavior can be achieved by directly referencing an 
#existing Series or sequence:
df = df.assign(temp_f=df['temp_c'] * 9 / 5 + 32)
print("\n",df)   
'''
In Python 3.6+, you can create multiple columns within the same assign 
where one of the columns depends on another one defined within the same assign:
'''
df = df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,
           temp_k=lambda x: (x['temp_f'] +  459.67) * 5 / 9)
print(df)