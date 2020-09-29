#DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

import pandas as pd
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                             pd.NaT]})
print(df,'\n')
'''
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
'''
print(df.dropna(),'\n') #by default how = 'any' and axis = 0 (row wise)
'''
     name        toy       born
1  Batman  Batmobile 1940-04-25
'''
print(df.dropna(axis=1),'\n')
'''
       name
0    Alfred
1    Batman
2  Catwoman 
'''

#now change how = 'all'
print(df.dropna(axis=0, how='all'),'\n')
'''
      name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
'''
print(df.dropna(axis=1, how='all'),'\n')
'''
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT 
'''
#Keep only the rows with at least 1 non-NA values.
print(df.dropna(thresh=1),'\n')
'''
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT 
'''
#Keep only the rows with at least 2 non-NA values.
print(df.dropna(thresh=2),'\n') 
'''
       name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT 
'''
#If subset columns has one NaN vlalue then this row is dorped
print(df.dropna(subset=['name','toy']))
'''
      name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
'''
print(df.dropna(axis = 1,subset=[0]))
'''
       name
0    Alfred
1    Batman
2  Catwoman
'''
print(df.dropna(axis = 1,subset=[1,2]))
'''
       name        toy
0    Alfred        NaN
1    Batman  Batmobile
2  Catwoman   Bullwhip
'''

print(df.dropna(axis = 1,subset=[0,2])) #same as subset[0]

#Keep the DataFrame with valid entries in the same variable.
print(df.dropna(inplace=False))
'''
     name        toy       born
1  Batman  Batmobile 1940-04-25
'''
print(df.dropna(inplace=True)) #output: None 

