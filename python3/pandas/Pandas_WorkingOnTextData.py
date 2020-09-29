import pandas as pd
import numpy as np
#Working with series data
ser = pd.Series(['a','v','nahid',np.nan,'AbaaB','Hassan','d'])
print(ser,"\n")
'''
Output:
0         a
1         v
2     nahid
3       NaN
4     AbaaB
5    Hassan
6         d
'''
#***************Converting to lowerCase and UpperCase**************
low = ser.str.lower()
print(low,"\n")
'''
Output:
0         a
1         v
2     nahid
3       NaN
4     abaab
5    hassan
6         d
'''
up = ser.str.upper()
print(up,"\n")
'''
Output:
0         A
1         V
2     NAHID
3       NaN
4     ABAAB
5    HASSAN
6         D
'''
#***************Getting length of each Element**********************
ln = ser.str.len()
print(ln,"\n")
'''
Output:
0    1.0
1    1.0
2    5.0
3    NaN
4    5.0
5    6.0
6    1.0
'''
#Working with indexes(Columns)
#The string method of index are especially usefull for cleaning up or 
#transforming DataFrame Columns. For instance, you may have columns with
#leading and trailing whitespaces

#***********Removing the leading and trailing whitespaces**********
#Using strip method
idx = pd.Index(['Name ', ' Hassan', 'Mony', ' Nahid '])
print(idx,"\n") #Index(['Name ', ' Hassan', 'Mony', ' Nahid '], dtype='object')
print(idx.str.strip(),"\n") #Index(['Name', 'Hassan', 'Mony', 'Nahid'], dtype='object') 

#*************Remove only Left leading whitespace******************
print(idx.str.lstrip(),"\n")
#Index(['Name ', 'Hassan', 'Mony', 'Nahid '], dtype='object') 

#****************Remove only Right trailing whitespaces*************
print(idx.str.rstrip(),"\n")
#Index(['Name', ' Hassan', 'Mony', ' Nahid'], dtype='object') 

#@@@@@@@@@@But after all if i print idx i show all the leading and trailing
#whiltespaces that's why i assign another variable
idx = idx.str.strip()
print(idx)
#Index(['Name', 'Hassan', 'Mony', 'Nahid'], dtype='object')
dict = {" Name":["Nahid", "Rafi", "Meem"],
        " Age ":[21,22,21],
        " Weight":[48,75,76],
        " Height":[5.3, 5.8, 5.6],
        " Sex ":['Male','Male','Male']}
df = pd.DataFrame(dict)
print("\n",df,"\n")
'''
Output:
     Name   Age    Weight   Height  Sex 
0  Nahid     21       48      5.3  Male
1   Rafi     22       75      5.8  Male
2   Meem     21       76      5.6  Male 
'''
print(df.columns,"\n")
#Index([' Name', ' Age ', ' Weight', ' Height', ' Sex '], dtype='object') 

'''We see that in columns heading name there are whitespaces
Since df.columns is an index obj, that's why we can use .str accessor'''

df.columns = df.columns.str.strip()
print(df.columns,"\n") #Index(['Name', 'Age', 'Weight', 'Height', 'Sex'], dtype='object')
print(df,"\n")
'''
Output:
    Name  Age  Weight  Height   Sex
0  Nahid   21      48     5.3  Male
1   Rafi   22      75     5.8  Male
2   Meem   21      76     5.6  Male 
'''

#**********Removing some unwanted characters form columns*************
dict = {" Person Name":["Nahid", "Rafi", "Meem"],
        "Person Age ":[21,22,21],
        "Person Weight":[48,75,76],
        "Person Height":[5.3, 5.8, 5.6],
        "Person Sex":['Male','Male','Male']}
df = pd.DataFrame(dict)

print(df,"\n")
'''
Output:
   Person Name  Person Age   Person Weight  Person Height Person Sex
0        Nahid           21             48            5.3       Male
1         Rafi           22             75            5.8       Male
2         Meem           21             76            5.6       Male 
'''
#we remove leading or trailing whitespaces using strip() and replace 
#Person_Name instead of Person Name using str.replace() Method
df.columns = df.columns.str.strip().str.replace(' ','_')
print(df.columns,"\n")
'''Index(['Person_Name', 'Person_Age', 'Person_Weight', 'Person_Height',
       'Person_Sex'],dtype='object')'''
print(df,"\n")
'''
  Person_Name  Person_Age  Person_Weight  Person_Height Person_Sex
0       Nahid          21             48            5.3       Male
1        Rafi          22             75            5.8       Male
2        Meem          21             76            5.6       Male
'''
#*****************spliting string columns**********************'''
ser = pd.Series(['a_b_c', 'B_C_d', np.nan, 'Nahid_Hassan']) 
ser = ser.str.split('_')
print(ser,"\n")
'''
0          [a, b, c]
1          [B, C, d]
2                NaN
3    [Nahid, Hassan]
'''
#**************************Don't spliting columns******************
#df.columns = df.columns.str.split('_')
#print(df.columns.str.split('_'))

#Becasue split() method return me a list but columns not a list

#******************Series: concatenation**************************
ser = pd.Series(['a','b','c','d'])
print(ser.str.cat(),"\n") #abcd
print(ser.str.cat(sep=','),"\n") #a,b,c,d
ser = pd.Series(['a','b',np.nan,'d'])
print(ser.str.cat(sep=','),"\n") #a,b,d 
#by default, missing values are ignored,using na_rep, then can be given
#a representation
print(ser.str.cat(sep=',',na_rep='-'),"\n") #a,b,-,d 

#******concatenating a series and something list-like into a series******
ser = ser.str.cat(['A','B','C','D']) #new series will append an each element
print(ser,"\n")
'''
0     aA
1     bB
2    NaN
3     dD
'''
#**********************Indexing with str*******************************
'''You can use [] notation to directly index by position locations. If you
Index past the end of the string, the result will be NaN'''

ser = pd.Series(['A', 'B', 'C', 'AaBb',np.nan, 'CaBa', 'dog', 'cat'])
print(ser[0],'\n') #A
print(ser.str[0],'\n')
'''
0      A
1      B
2      C
3      A
4    NaN
5      C
6      d
7      c
'''
print(ser.str[1],'\n')
'''
0    NaN
1    NaN
2    NaN
3      a
4    NaN
5      a
6      o
7      a
'''
#***************Testing for string that match or contain a pattern********
pattern = '[0-9][a-z]'
ser = pd.Series(['1','2','2a','a2a','a2','22cc'])
print(ser.str.contains(pattern),"\n") #true if individual elements are contains
'''
0    False
1    False
2     True
3     True
4    False
5     True
'''
print(ser.str.match(pattern),'\n') #true if individual elements are strictly match
'''
0    False
1    False
2     True
3    False
4    False
5    False
'''
ser = pd.Series(['1','2','2a','a2a','2aa2','2cc'])
print(ser.str.match(pattern),"\n")
'''
0    False
1    False
2     True
3    False
4     True
5     True
'''

#**********************Join()******************************************
ser = pd.Series([['nahid', 'hassan', 'mony'],
                 ['karim', 1.5, 'selim'],
                 [1.3,4.5,3.1],
                 ['apple', 'microsoft', 1.5],
                 ['google', 'facebook', '1.6']])
ser =ser.str.join('-')
print(ser,'\n')
'''
0      nahid-hassan-mony
1                    NaN
2                    NaN
3                    NaN
4    google-facebook-1.6
'''