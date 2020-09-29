import pandas as pd

df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
pd.set_option('max_rows',5)
print(df)
'''
     company  numEmps category    ...    state fundedDate raisedAmt
0   LifeLock      NaN      web    ...       AZ   1-May-07   6850000
1   LifeLock      NaN      web    ...       AZ   1-Oct-06   6000000
..       ...      ...      ...    ...      ...        ...       ...
97    MeeVee      NaN      web    ...       CA   1-Feb-06   6500000
98    MeeVee      NaN      web    ...       CA   1-Aug-06   8000000
'''

#*****************most basic indexing using [] **********************
#1- passing a single column name
print(df['fundedDate']) #printing only a single column value
'''
0     1-May-07
1     1-Oct-06
  
97    1-Feb-06
98    1-Aug-06
Name: fundedDate, Length: 99, dtype: object
'''
#2- passing multiple columns names, passing a list of columns name
print(df[['company','numEmps','raisedAmt']]) #printing 3 columns value
'''
     company  numEmps  raisedAmt
0   LifeLock      NaN    6850000
1   LifeLock      NaN    6000000
..       ...      ...        ...
97    MeeVee      NaN    6500000
98    MeeVee      NaN    8000000
'''
#If columns name is not contained in the DataFrame, an exception will be raised
#print(df['name']) #show error....! 
df['numEmps'] = df['raisedAmt'] #assigning one column value to another
print(df['numEmps'])
'''
0     6850000
1     6000000
  
97    6500000
98    8000000
Name: numEmps, Length: 99, dtype: int64
'''
print(df.head()) #Now see original dataframe is changed
'''
       company   numEmps category    ...    state fundedDate raisedAmt
0     LifeLock   6850000      web    ...       AZ   1-May-07   6850000
1     LifeLock   6000000      web    ...       AZ   1-Oct-06   6000000
2     LifeLock  25000000      web    ...       AZ   1-Jan-08  25000000
3  MyCityFaces     50000      web    ...       AZ   1-Jan-08     50000
4     Flypaper   3000000      web    ...       AZ   1-Feb-08   3000000
'''
#****************************practical example**************************
dict = {"Name":pd.Series(["Nahid", "Rafi", "Meem"]),
        "Age":pd.Series([21,22,21]),
        "Weight":pd.Series([48,75,76]),
        "Height":pd.Series([5.3, 5.8, 5.6])}
df = pd.DataFrame(dict)

df[['Age','Weight']] = df[['Weight','Age']] #swap Age and weight 
#or assigning age, weight to weight and age
print(df.head())
'''
    Name  Age  Weight  Height
0  Nahid   48      21     5.3
1   Rafi   75      22     5.8
2   Meem   76      21     5.6
'''
#Assigning a scaler value in a column
df['Weight'] = 65
print(df.tail())
'''
    Name  Age  Weight  Height
0  Nahid   48      65     5.3
1   Rafi   75      65     5.8
2   Meem   76      65     5.6
'''

#**************************#slicing#***************************
#slicing row only
data = {'Name':['Nahid','Hassan', 'Mursalin', 'Rafi', 'Rakib'],
        'Year':[2018,2018,2018,2018,2018],
        'Income':['5 core','10 core','3 core','7 core','6 core'],
        'Age':[21,22,21,22,23],
        'Sex':['Male','Male','Male','Male','Male'],
        }
df = pd.DataFrame(data)
pd.set_option('max_rows',6)
print(df[:]) #slicing
'''
       Name  Year   Income  Age   Sex
0     Nahid  2018   5 core   21  Male
1    Hassan  2018  10 core   22  Male
2  Mursalin  2018   3 core   21  Male
3      Rafi  2018   7 core   22  Male
4     Rakib  2018   6 core   23  Male
'''
print(df[:2])
'''
     Name  Year   Income  Age   Sex
0   Nahid  2018   5 core   21  Male
1  Hassan  2018  10 core   22  Male
'''
print(df[2:])
'''
       Name  Year  Income  Age   Sex
2  Mursalin  2018  3 core   21  Male
3      Rafi  2018  7 core   22  Male
4     Rakib  2018  6 core   23  Male
'''

#**********using number of steps you want to skipped***********
#df[start:end:step]

print(df[0:4:1])
'''
       Name  Year   Income  Age   Sex
0     Nahid  2018   5 core   21  Male
1    Hassan  2018  10 core   22  Male
2  Mursalin  2018   3 core   21  Male
3      Rafi  2018   7 core   22  Male
'''
'''Printing the records bottom to top'''
print(df[::-1]) #-1 indicates reverse order
'''
       Name  Year   Income  Age   Sex
4     Rakib  2018   6 core   23  Male
3      Rafi  2018   7 core   22  Male
2  Mursalin  2018   3 core   21  Male
1    Hassan  2018  10 core   22  Male
0     Nahid  2018   5 core   21  Male
'''