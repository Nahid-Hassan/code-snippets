import pandas as pd

data = {'Name':['nahid', 'rafi', 'meem','himu', 'minhaz'],
        'Sex':['male', 'male','male', 'male','male'],
        'Year':[2018,2018,2018,2018,2018],
        'Income':['10 core','7 core','5 core','12 core','7 core'],
        'Age':[22,23,21,22,20]
        }

df = pd.DataFrame(data)

#.iloc[start row idx : end row idx, start column idx : end column idx]
print(df.iloc[:4,:3]) #Actual end index = end index - 1
'''
   Name   Sex  Year
0  nahid  male  2018
1   rafi  male  2018
2   meem  male  2018
3   himu  male  2018
'''
#But!!!
print(df.loc[:4,'Name':'Income']) #Actual end index = mentioned index
'''
     Name   Sex  Year   Income
0   nahid  male  2018  10 core
1    rafi  male  2018   7 core
2    meem  male  2018   5 core
3    himu  male  2018  12 core
4  minhaz  male  2018   7 core
'''
#You can also fetch a single row value
print(df.iloc[0])
'''
Name        nahid
Sex          male
Year         2018
Income    10 core
Age            22
'''
print(df.iloc[1])
'''
Name        rafi
Sex         male
Year        2018
Income    7 core
Age           23
'''

#Assigning a scaler value to a row:
df.iloc[2] = 50
print(df)
'''
     Name   Sex  Year   Income  Age
0   nahid  male  2018  10 core   22
1    rafi  male  2018   7 core   23
2      50    50    50       50   50 #this row is fully changed by scaler value
3    himu  male  2018  12 core   22
4  minhaz  male  2018   7 core   20
'''

#cAssigning a scaler value ofa column
df.iloc[:,3] = 'No Income'
print(df.iloc[:,:])
'''
     Name   Sex  Year     Income  Age
0   nahid  male  2018  No Income   22
1    rafi  male  2018  No Income   23
2      50    50    50  No Income   50
3    himu  male  2018  No Income   22
4  minhaz  male  2018  No Income   20
'''

df = pd.DataFrame(data, index=[4,3,2,0,1])
print(df)
'''
     Name   Sex  Year   Income  Age
4   nahid  male  2018  10 core   22
3    rafi  male  2018   7 core   23
2    meem  male  2018   5 core   21
0    himu  male  2018  12 core   22
1  minhaz  male  2018   7 core   20
'''
#You can also used an interger list in a .iloc[]
print(df.iloc[[0,1,3,4],[0,2,3, 4]])
'''
     Name  Year   Income  Age
4   nahid  2018  10 core   22
3    rafi  2018   7 core   23
0    himu  2018  12 core   22
1  minhaz  2018   7 core   20
'''
#print(df.iloc[0,1, 7]) #7 is not here in dataframe row index so this given an error
#But
print(df.iloc[:12]) #is working fine it shows 0 to 12-1 = 11
'''
     Name   Sex  Year   Income  Age
4   nahid  male  2018  10 core   22
3    rafi  male  2018   7 core   23
2    meem  male  2018   5 core   21
0    himu  male  2018  12 core   22
1  minhaz  male  2018   7 core   20
'''