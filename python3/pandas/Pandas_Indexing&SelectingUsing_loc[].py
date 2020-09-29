#selection by level
#.loc[row start idx : row end idx, column start name : column end name]

import pandas as pd

data = {'Name':['Nahid','Hassan', 'Mursalin', 'Rafi', 'Rakib'],
        'Year':[2018,2018,2018,2018,2018],
        'Income':['5 core','10 core','3 core','7 core','6 core'],
        'Age':[21,22,21,22,23],
        'Sex':['Male','Male','Male','Male','Male'],
        
df = pd.DataFrame(data)
pd.set_option('max_rows',10) #show max 10 rows

print(df.loc[:,:]) #Going to display all rows and all columns
'''
       Name  Year   Income  Age   Sex
0     Nahid  2018   5 core   21  Male
1    Hassan  2018  10 core   22  Male
2  Mursalin  2018   3 core   21  Male
3      Rafi  2018   7 core   22  Male
4     Rakib  2018   6 core   23  Male
'''
print(df.loc[:2]) #show 0-2 idx but general inx sysytem it shows 0 to 1 idx 
'''
       Name  Year   Income  Age   Sex
0     Nahid  2018   5 core   21  Male
1    Hassan  2018  10 core   22  Male
2  Mursalin  2018   3 core   21  Male
'''
#Display ros 0 to 2 and columns Name to Income
print(df.loc[:2,'Name':'Income'])
'''
       Name  Year   Income
0     Nahid  2018   5 core
1    Hassan  2018  10 core
2  Mursalin  2018   3 core
'''

#****************Selecting a single row and single column***************
print(df.loc[5:5]) #Empty DataFrame
print(df.loc[4:4])
'''
    Name  Year  Income  Age   Sex
4  Rakib  2018  6 core   23  Male
'''
print(df.loc[:,'Name'])
'''
0       Nahid
1      Hassan
2    Mursalin
3        Rafi
4       Rakib
'''

#**************assigning a value to particular row and column************
df.loc[:,'Age'] = 21
print(df.loc[:,:])
'''
       Name  Year   Income  Age   Sex
0     Nahid  2018   5 core   21  Male
1    Hassan  2018  10 core   21  Male
2  Mursalin  2018   3 core   21  Male
3      Rafi  2018   7 core   21  Male
4     Rakib  2018   6 core   21  Male
'''

#****************A list or array of labels inside loc***************
print(df.loc[:2,['Name', 'Income']])
'''
       Name   Income
0     Nahid   5 core
1    Hassan  10 core
2  Mursalin   3 core
'''
print(df.loc[[0,2,4],['Name', 'Age', 'Income']])
'''
       Name  Age  Income
0     Nahid   21  5 core
2  Mursalin   21  3 core
4     Rakib   21  6 core
'''
df.loc[:,'Age'] = [21 , 17, 23, 20, 27]
#***************For getting valuse for a boolean array*******************
print(df.loc[:,'Age'] > 20)
'''
0     True
1    False
2     True
3    False
4     True
'''
print(df.loc[df.loc[:,'Age']>20]) #print all the rows having age > 20
'''
       Name  Year  Income  Age   Sex
0     Nahid  2018  5 core   21  Male
2  Mursalin  2018  3 core   23  Male
4     Rakib  2018  6 core   27  Male
'''
print(df.loc[df.loc[:,'Age']>20,'Age':'Age']) #display only age column
'''
   Age
0   21
2   23
4   27
'''
print(df.loc[df.loc[:,'Age']>20,['Age']]) #display only age column using list
'''
   Age
0   21
2   23
4   27
'''
#**********************Getting a particular cell value"**********************
print(df.loc[4,'Name']) #Rakib

#***************sorting a particular column*************************
df = pd.DataFrame(data, index=[5,4,1,2,3])
print(df)
'''
       Name  Year   Income  Age   Sex
5     Nahid  2018   5 core   21  Male
4    Hassan  2018  10 core   22  Male
1  Mursalin  2018   3 core   21  Male
2      Rafi  2018   7 core   22  Male
3     Rakib  2018   6 core   23  Male
'''
df = df.sort_index() #sort index value
print(df.head())
'''
       Name  Year   Income  Age   Sex
1  Mursalin  2018   3 core   21  Male
2      Rafi  2018   7 core   22  Male
3     Rakib  2018   6 core   23  Male
4    Hassan  2018  10 core   22  Male
5     Nahid  2018   5 core   21  Male
'''
