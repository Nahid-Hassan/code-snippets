'''
DataFrame.sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs)

Return the sum of the values for the requested axis.
This is the equivalent method of numpy.sum()
'''
import pandas as pd
import keras as k

df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
# https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
print(df.head(), "\n")
'''
  Company Name  Worker Number  amount  Transection  raisedAmt
0     LifeLock            NaN   10121        10121    6850000
1     LifeLock            NaN   12133        12133    6000000
2     LifeLock         2323.0   23232         1121   25000000
3  MyCityFaces            7.0    3222          232      50000
4     Flypaper            NaN      12           12    3000000 
'''


# *************Argument 1:--> axis: {index(0), columns(1)}*************
print(df.sum(axis=0))  # axis = 0 incating columns wise sum
'''
Company Name     LifeLockLifeLockLifeLockMyCityFacesFlypaperInf...
Worker Number                                                 2476
amount                                                       49000
Transection                                                  43961
raisedAmt                                                 50523750
'''
print(df.sum(axis=1))  # axis = 1 incating row wise sum
'''
0     6870242.0
1     6024266.0
2    25026676.0
3       53461.0
4     3000024.0
5     9013259.0
6      250370.0
7      143671.0
8      237218.0
'''

# *************Argument 2:--> skipna = Boolean, by default = ture*************
# If skipna=True not consider NaN value, Adding others values without NaN
print(df.sum(axis=0, skipna=True))
'''
Company Name     LifeLockLifeLockLifeLockMyCityFacesFlypaperInf...
Worker Number                                                 2476
amount                                                       49000
Transection                                                  43961
raisedAmt                                                 50523750
'''
# If skipna=False consider NaN value or empty value, Output is NaN
print(df.sum(axis=0, skipna=False))
'''
Company Name     LifeLockLifeLockLifeLockMyCityFacesFlypaperInf...
Worker Number                                                  NaN
amount                                                       49000
Transection                                                  43961
raisedAmt                                                 50523750
'''
# Now for row wise sum axis = 1
print(df.sum(axis=1, skipna=True))
'''
0     6870242.0
1     6024266.0
2    25026676.0
3       53461.0
4     3000024.0
5     9013259.0
6      250370.0
7      143671.0
8      237218.0
'''
print(df.sum(axis=1, skipna=False))
'''
0           NaN
1           NaN
2    25026676.0
3       53461.0
4           NaN
5     9013259.0
6      250370.0
7      143671.0
8      237218.0
'''
# *************Argument 3:--> numeric_only: boolean, default none *************
# If numeric_only is ture then it calculate only the column or raw that is all int
# it can not calculate both string integer it's only calculate int to int string to string
print(df.sum(axis=0, skipna=True, numeric_only=True))
'''
Worker Number        2476.0
amount              49000.0
Transection         43961.0
raisedAmt        50523750.0
'''
# If numeric_only is false then show an error when a column or raw has str and int both
#print(df.sum(axis=0, skipna=True, numeric_only=False))
'''
    .....................................  
    File "/home/nahid/anaconda3/lib/python3.7/site-packages/pandas/core/nanops.py", line 77, in _f
      return f(*args, **kwargs)
    File "/home/nahid/anaconda3/lib/python3.7/site-packages/pandas/core/nanops.py", line 336, in nansum
      the_sum = values.sum(axis, dtype=dtype_sum)

    File "/home/nahid/anaconda3/lib/python3.7/site-packages/numpy/core/_methods.py", line 36, in _sum
      return umr_sum(a, axis, dtype, out, keepdims, initial)

TypeError: can only concatenate str (not "int") to str
'''
#print(df.sum(axis=1, skipna=True, numeric_only=True))
'''TypeError: can only concatenate str (not "int") to str'''
# So your .csv file need to rewrite

# Anther example:
data = {'name': ['Md. nahid', ' hasan', ' mony.']}
df1 = pd.DataFrame(data)
print(df1.head())
'''
        name
0  Md. nahid
1      hasan
2      mony.
'''
print(df1.sum(numeric_only=False))  # name    Md. nahid hasan mony.
# Series([], dtype: float64) can not calculate
print(df1.sum(numeric_only=True))

# *************Argument 4:--> min_count: int, default 0 *************
# Column wise sum and Checking whether a column is having 15 number of non NA Values 
# is not sum will be NaN
print(df.sum(axis=0,numeric_only = True, min_count=7))
'''
Worker Number           NaN
amount              49000.0
Transection         43961.0
raisedAmt        50523750.0
'''
print(df.sum(axis=1,numeric_only = True, min_count=4))
'''
0           NaN
1           NaN
2    25026676.0
3       53461.0
4           NaN
5     9013259.0
6      250370.0
7      143671.0
8      237218.0
'''

# *************Argument 5:--> level: int or level name, default none **********
data = {'Country':['Bangladesh', 'India', 'Pakistan', 'Srilanka', 'England'],
        'Game':['Cricket', 'Cricket','Cricket', 'Cricket','Footbal'],
        'Master Players':['Sakib', 'Sachin', 'Imran kahn', 'Sangakara', 'Runi'],
        'Income':[110, 120, 190, 234,900],
        'Game Played':[123,234,232, 123,344],
        'Best Score':[425,234,232,341, 321]}
df = pd.DataFrame(data)
print(df)
'''
      Country     Game Master Players  Income  Game Played  Best Score
0  Bangladesh  Cricket          Sakib     110          123         425
1       India  Cricket         Sachin     120          234         234
2    Pakistan  Cricket     Imran kahn     190          232         232
3    Srilanka  Cricket      Sangakara     234          123         341
4     England  Footbal           Runi     900          344         321
'''
print(df.sum())
'''
Country           BangladeshIndiaPakistanSrilankaEngland
Game                 CricketCricketCricketCricketFootbal
Master Players        SakibSachinImran kahnSangakaraRuni
Income                                              1554
Game Played                                         1056
Best Score                                          1553
'''
print(df.sum(numeric_only=True))
'''
Income         1554
Game Played    1056
Best Score     1553
'''
#Don't understood clearly min_count option
print(df.sum(numeric_only=True, min_count = 1, axis = 1))

#Create Multiple Index
data = {'Country':['Bangladesh', 'Bangladesh', 'India', 'India', 'Srilanka'],
        'Game':['Cricket', 'Kabadi','Cricket', 'Ragbi','Cricket'],
        'Master Players':['Sakib', 'Masud', 'Sachin', 'Murad', 'Sangakara'],
        'Income':[110, 120, 190, 234,900],
        'Game Played':[123,234,232, 123,344],
        'Best Score':[425,234,232,341, 321]}
df = pd.DataFrame(data)
print(df)

newDf = df.set_index(['Country', 'Game'], drop=True)
print(newDf)    
#If drop = True not added Country and Game Column
'''
                   Master Players  Income  Game Played  Best Score
Country    Game                                                   
Bangladesh Cricket          Sakib     110          123         425
           Kabadi           Masud     120          234         234
India      Cricket         Sachin     190          232         232
           Ragbi            Murad     234          123         341
Srilanka   Cricket      Sangakara     900          344         321
'''
#if drop = False added Country and Game column
newDf = df.set_index(['Country', 'Game'], drop=False)
print(newDf)    
'''
                       Country     Game  ... Game Played  Best Score
Country    Game                          ...                        
Bangladesh Cricket  Bangladesh  Cricket  ...         123         425
           Kabadi   Bangladesh   Kabadi  ...         234         234
India      Cricket       India  Cricket  ...         232         232
           Ragbi         India    Ragbi  ...         123         341
Srilanka   Cricket    Srilanka  Cricket  ...         344         321
'''
#If you have multiple index dataframe then you used labeled as an argument
#lets do this some sum operations
print(newDf.sum(axis=0, numeric_only=True))
'''
Income         1554
Game Played    1056
Best Score     1553
'''
print(newDf.sum(axis=1, numeric_only=True))
'''
Country     Game   
Bangladesh  Cricket     658
            Kabadi      588
India       Cricket     654
            Ragbi       698
Srilanka    Cricket    1565
'''
print(newDf.sum(level=0)) #Grouping the values based on country
'''
            Income  Game Played  Best Score
Country                                    
Bangladesh     230          357         659
India          424          355         573
Srilanka       900          344         321
'''
print(newDf.sum(level=1)) #Grouping the values based on Game
'''
         Income  Game Played  Best Score
Game                                    
Cricket    1200          699         978
Kabadi      120          234         234
Ragbi       234          123         341
'''