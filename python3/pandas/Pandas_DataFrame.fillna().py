#DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
#Date 16-04-19; Time: 2:33 AM

import numpy as np
import pandas as pd

#@@@@@@@@@@@@@ value atrribute@@@@@@@@@@@@
df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
print(df,'\n')
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

#value: scalar, dict, Series, DataFrame
df_new = df.fillna(value=0)
print(df_new,'\n')
'''
   Company Name  Worker Number   amount  Transection   raisedAmt name/num
0        LifeLock            0.0  10121.0      10121.0   6850000.0    nahid
1        LifeLock            0.0  12133.0      12133.0         0.0        0
2        LifeLock         2323.0      0.0       1121.0  25000000.0     mony
3     MyCityFaces            7.0   3222.0          0.0     50000.0        0
4        Flypaper            0.0     12.0         12.0         0.0  musalin
5    Infusionsoft          105.0     23.0      13131.0   9000000.0        0
6           gAuto            4.0      0.0          0.0    250000.0     himu
7  ChosenList.com            5.0    232.0       3434.0    140000.0  minahaz
8  ChosenList.com           32.0      2.0       3434.0    233750.0    rajib 
'''

comanyNameMode = df['Company Name'].mode()[0]
workerNumberMean = df['Worker Number'].mean()
amountMean = df['amount'].mean()
transectionMean = df['Transection'].mean()
raisedAmtMedian = df['raisedAmt'].median()
nameNumMode = df['name/num'].mode()[0]

newDict = {'Company Name':comanyNameMode,
            'Worker Number':workerNumberMean,
            'amount':amountMean,
            'Transection':transectionMean,
            'raisedAmt':raisedAmtMedian,
            'name/num':nameNumMode}

print((df.isnull().sum()/len(df)) * 100)
'''
Company Name      0.000000
Worker Number    33.333333
amount           22.222222
Transection      22.222222
raisedAmt        22.222222
name/num         33.333333
'''
print('\n', newDict)
'''
{'Company Name': 'LifeLock', 'Worker Number': 412.6666666666667, 
'amount': 3677.8571428571427, 'Transection': 6198.0, 
'raisedAmt': 250000.0, 'name/num': 'himu'}
'''

new_df = df.fillna(value=newDict)
print('\n',new_df)
'''

      Company Name  Worker Number        amount  Transection   raisedAmt name/num
0        LifeLock     412.666667  10121.000000      10121.0   6850000.0    nahid
1        LifeLock     412.666667  12133.000000      12133.0    250000.0     himu
2        LifeLock    2323.000000   3677.857143       1121.0  25000000.0     mony
3     MyCityFaces       7.000000   3222.000000       6198.0     50000.0     himu
4        Flypaper     412.666667     12.000000         12.0    250000.0  musalin
5    Infusionsoft     105.000000     23.000000      13131.0   9000000.0     himu
6           gAuto       4.000000   3677.857143       6198.0    250000.0     himu
7  ChosenList.com       5.000000    232.000000       3434.0    140000.0  minahaz
8  ChosenList.com      32.000000      2.000000       3434.0    233750.0    rajib
'''
print((new_df.isnull().sum()/len(new_df)) * 100)
'''
Company Name     0.0
Worker Number    0.0
amount           0.0
Transection      0.0
raisedAmt        0.0
name/num         0.0
'''

#@@@@@@@@@@@@@ Method atrribute @@@@@@@@@@@@
print(df,'\n')
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
new_df = df.fillna(method='bfill')
print(new_df,'\n')
'''
     Company Name  Worker Number   amount  Transection   raisedAmt name/num
0        LifeLock         2323.0  10121.0      10121.0   6850000.0    nahid
1        LifeLock         2323.0  12133.0      12133.0  25000000.0     mony
2        LifeLock         2323.0   3222.0       1121.0  25000000.0     mony
3     MyCityFaces            7.0   3222.0         12.0     50000.0  musalin
4        Flypaper          105.0     12.0         12.0   9000000.0  musalin
5    Infusionsoft          105.0     23.0      13131.0   9000000.0     himu
6           gAuto            4.0    232.0       3434.0    250000.0     himu
7  ChosenList.com            5.0    232.0       3434.0    140000.0  minahaz
8  ChosenList.com           32.0      2.0       3434.0    233750.0    rajib
'''

new_df = df.fillna(method='ffill')
print(new_df,'\n')
'''
     Company Name  Worker Number   amount  Transection   raisedAmt name/num
0        LifeLock            NaN  10121.0      10121.0   6850000.0    nahid
1        LifeLock            NaN  12133.0      12133.0   6850000.0    nahid
2        LifeLock         2323.0  12133.0       1121.0  25000000.0     mony
3     MyCityFaces            7.0   3222.0       1121.0     50000.0     mony
4        Flypaper            7.0     12.0         12.0     50000.0  musalin
5    Infusionsoft          105.0     23.0      13131.0   9000000.0  musalin
6           gAuto            4.0     23.0      13131.0    250000.0     himu
7  ChosenList.com            5.0    232.0       3434.0    140000.0  minahaz
8  ChosenList.com           32.0      2.0       3434.0    233750.0    rajib 
'''
print((new_df.isnull().sum()/len(new_df)) * 100)
'''
Company Name      0.000000
Worker Number    22.222222
amount            0.000000
Transection       0.000000
raisedAmt         0.000000
name/num          0.000000
'''
#@@@@@@@@@@@@@@@@ axis attribute @@@@@@@@@@@@
new_df = df.fillna(method='ffill', axis = 1) #0 for rows 1 for columns
print('\n',new_df)
'''
      Company Name Worker Number amount Transection raisedAmt name/num
0        LifeLock      LifeLock  10121       10121  6.85e+06    nahid
1        LifeLock      LifeLock  12133       12133     12133    12133
2        LifeLock          2323   2323        1121   2.5e+07     mony
3     MyCityFaces             7   3222        3222     50000    50000
4        Flypaper      Flypaper     12          12        12  musalin
5    Infusionsoft           105     23       13131     9e+06    9e+06
6           gAuto             4      4           4    250000     himu
7  ChosenList.com             5    232        3434    140000  minahaz
8  ChosenList.com            32      2        3434    233750    rajib
'''

new_df = df.fillna(method='bfill', limit=1)
print('\n',new_df)
'''
      Company Name  Worker Number   amount  Transection   raisedAmt name/num
0        LifeLock            NaN  10121.0      10121.0   6850000.0    nahid
1        LifeLock         2323.0  12133.0      12133.0  25000000.0     mony
2        LifeLock         2323.0   3222.0       1121.0  25000000.0     mony
3     MyCityFaces            7.0   3222.0         12.0     50000.0  musalin
4        Flypaper          105.0     12.0         12.0   9000000.0  musalin
5    Infusionsoft          105.0     23.0      13131.0   9000000.0     himu
6           gAuto            4.0    232.0       3434.0    250000.0     himu
7  ChosenList.com            5.0    232.0       3434.0    140000.0  minahaz
8  ChosenList.com           32.0      2.0       3434.0    233750.0    rajib
'''

new_df = df.fillna(method='bfill', inplace=True)
print(df) #notice i print df 
'''
     Company Name  Worker Number   amount  Transection   raisedAmt name/num
0        LifeLock         2323.0  10121.0      10121.0   6850000.0    nahid
1        LifeLock         2323.0  12133.0      12133.0  25000000.0     mony
2        LifeLock         2323.0   3222.0       1121.0  25000000.0     mony
3     MyCityFaces            7.0   3222.0         12.0     50000.0  musalin
4        Flypaper          105.0     12.0         12.0   9000000.0  musalin
5    Infusionsoft          105.0     23.0      13131.0   9000000.0     himu
6           gAuto            4.0    232.0       3434.0    250000.0     himu
7  ChosenList.com            5.0    232.0       3434.0    140000.0  minahaz
8  ChosenList.com           32.0      2.0       3434.0    233750.0    rajib
'''
