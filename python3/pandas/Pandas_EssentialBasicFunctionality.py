#Read .csv (coma separated value) file and modify it
import pandas as pd

df = pd.read_csv('/media/nahid/New Volume/GitHub/Pandas/sample.csv')
print(df,"\n")
'''
Output:
          company  numEmps  category        city state fundedDate  raisedAmt
0        LifeLock      NaN       web       Tempe    AZ   1-May-07    6850000
1        LifeLock      NaN       web       Tempe    AZ   1-Oct-06    6000000
2        LifeLock      NaN       web       Tempe    AZ   1-Jan-08   25000000
3     MyCityFaces      7.0       web  Scottsdale    AZ   1-Jan-08      50000
4        Flypaper      NaN       web     Phoenix    AZ   1-Feb-08    3000000
5    Infusionsoft    105.0  software     Gilbert    AZ   1-Oct-07    9000000
6           gAuto      4.0       web  Scottsdale    AZ   1-Jan-08     250000
7  ChosenList.com      5.0       web  Scottsdale    AZ   1-Oct-06     140000
8  ChosenList.com      5.0       web  Scottsdale    AZ  25-Jan-08     233750
'''
#***************************Use head method****************************
print(df.head(),"\n") #by default it shows first 5 line of .csv file
#head() method can taken parameter --> DataFrame.head(n=5)
#n say how many lines are showing 

print(df.head(3),"\n")
'''
Output:
    company  numEmps category   city state fundedDate  raisedAmt
0  LifeLock      NaN      web  Tempe    AZ   1-May-07    6850000
1  LifeLock      NaN      web  Tempe    AZ   1-Oct-06    6000000
2  LifeLock      NaN      web  Tempe    AZ   1-Jan-08   25000000
'''
#*********************DataFrame.tail(n=5)*****************************
'''
Return the last n rows. This function returns last n rows from the 
object based on position. It is useful for quickly verifying data, 
for example, after sorting or appending rows.
'''
print(df.tail(4),"\n") #by default n = 5 
'''
Output:
          company  numEmps  category    ...    state fundedDate raisedAmt
5    Infusionsoft    105.0  software    ...       AZ   1-Oct-07   9000000
6           gAuto      4.0       web    ...       AZ   1-Jan-08    250000
7  ChosenList.com      5.0       web    ...       AZ   1-Oct-06    140000
8  ChosenList.com      5.0       web    ...       AZ  25-Jan-08    233750
'''
#*************shape, size, index, columns method*********************
print(df.shape,"\n") #(9, 7) 
print(df.size,"\n") #63
print(df.index,"\n") #RangeIndex(start=0, stop=9, step=1) 
print(df.columns,"\n") 
'''
Output:
Index(['company', 'numEmps', 'category', 'city', 'state', 'fundedDate',
       'raisedAmt'],
      dtype='object')
'''