import pandas as pd

df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
print((df.isnull().sum(axis=1))>1)
print(df[(df.isnull().sum(axis=1))>1])
'''
This are the rows that's contains at least 2 missing values

  Company Name  Worker Number   amount  Transection  raisedAmt name/num
1     LifeLock            NaN  12133.0      12133.0        NaN      NaN
3  MyCityFaces            7.0   3222.0          NaN    50000.0      NaN
4     Flypaper            NaN     12.0         12.0        NaN  musalin
6        gAuto            4.0      NaN          NaN   250000.0     himu
'''
newDf = df[(df.isnull().sum(axis=1))>1]
print('Percentage of missing values at least two in a rows = ',(len(newDf)/len(df))*100)
#Percentage of missing values at least two in a rows =  44.44444444444444

print('Percentage of missing non values at least two in a rows = ',(1-(len(newDf)/len(df)))*100)