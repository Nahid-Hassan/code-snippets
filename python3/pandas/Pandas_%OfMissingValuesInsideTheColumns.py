import pandas as pd

df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
print(df)
'''
     Company Name  Worker Number   amount  Transection   raisedAmt name/num
0        LifeLock            NaN  10121.0      10121.0   6850000.0    nahid
1        LifeLock            NaN  12133.0      12133.0         NaN      NaN
2        LifeLock         2323.0      NaN       1121.0  25000000.0     mony
3     MyCityFaces            7.0   3222.0          NaN     50000.0      NaN
4        Flypaper            NaN     12.0         12.0         NaN  musalin
5    Infusionsoft          105.0     23.0      13131.0   9000000.0      NaN
6           gAuto            4.0      NaN          NaN    250000.0     himu
7  ChosenList.com            5.0    232.0       3434.0    140000.0  minahaz
8  ChosenList.com           32.0      2.0       3434.0    233750.0    rajib
'''
#isnull function ture if value is missing otherwise false
print(df.isnull())
'''
   Company Name  Worker Number  amount  Transection  raisedAmt  name/num
0         False           True   False        False      False     False
1         False           True   False        False       True      True
2         False          False    True        False      False     False
3         False          False   False         True      False      True
4         False           True   False        False       True     False
5         False          False   False        False      False      True
6         False          False    True         True      False     False
7         False          False   False        False      False     False
8         False          False   False        False      False     False
'''
#We know boolean true 1 and false 0 so calculated the missing value
print(df.isnull().sum())
'''
Company Name     0
Worker Number    3
amount           2
Transection      2
raisedAmt        2
name/num         3
'''

#print % of missing values
print((df.isnull().sum() / len(df)) * 100)
'''
Company Name      0.000000
Worker Number    33.333333
amount           22.222222
Transection      22.222222
raisedAmt        22.222222
name/num         33.333333
'''