# DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')[source]
# Replace values given in to_replace with value.
# Date 16-04-19; Time: 3:41 PM

import pandas as pd
import numpy as np

df = pd.read_csv(
    '/media/nahid/New Volume/GitHub/Pandas/Replace Method Dataset.csv')
print(df, '\n')
'''
    Name  Height  Wight    BPM    Income Dibetic or Not
0   Nahid  165 cm     47     60   6850000             No
1  Hassan  176 cm     46     55     12121            Yes
2    Himu  165 cm     53     80  25000000             No
3    Meem   #####     76     75     50000            NaN
4  Minhaz   #####     75  $$$$$       ###            Yes
5    Rafi   #####     75     72   9000000            Yes
6    Moni  165 cm  $$$$$    NaN    250000             No 
'''
new_df = df.replace(to_replace=['#####', '###', '$$$$$'], value=np.NaN)
print(new_df, '\n')
'''
     Name  Height Wight  BPM    Income Dibetic or Not
0   Nahid  165 cm    47   60   6850000             No
1  Hassan  176 cm    46   55     12121            Yes
2    Himu  165 cm    53   80  25000000             No
3    Meem     NaN    76   75     50000            NaN
4  Minhaz     NaN    75  NaN       NaN            Yes
5    Rafi     NaN    75   72   9000000            Yes
6    Moni  165 cm   NaN  NaN    250000             No
'''
# Replace value with specific column
print(df.columns, '\n')
#Index(['Name', 'Height', 'Wight', 'BPM', 'Income', 'Dibetic or Not'], dtype='object')
dict_replace = {
    'Height': '#####',
    'Weight': '$$$$$',
    'BPM': '$$$$$',
    'Income': '###'
}

new_df = df.replace(to_replace=dict_replace, value=np.NaN)
print(new_df, '\n')
'''
     Name  Height Wight  BPM    Income Dibetic or Not
0   Nahid  165 cm    47   60   6850000             No
1  Hassan  176 cm    46   55     12121            Yes
2    Himu  165 cm    53   80  25000000             No
3    Meem     NaN    76   75     50000            NaN
4  Minhaz     NaN    75  NaN       NaN            Yes
5    Rafi     NaN    75   72   9000000            Yes
6    Moni  165 cm   NaN  NaN    250000             No 
'''

#Replace the unit of measurements in columns with blank
#regex=regular expression

dict_regex = {
    'Height':['A-Za-z'],
    'Weight': ['A-Za-z'],
    'Dibetic or Not': ['A-Za-z'],
}       
#don't understand
new_df = df.replace(to_replace=dict_regex, value='', regex=True)
print(new_df, '\n')

new_df = df.replace(to_replace=['#####','$$$$$','###'],method='ffill')
print(new_df,'\n')
'''
     Name  Height Wight  BPM    Income Dibetic or Not
0   Nahid  165 cm    47   60   6850000             No
1  Hassan  176 cm    46   55     12121            Yes
2    Himu  165 cm    53   80  25000000             No
3    Meem  165 cm    76   75     50000            NaN
4  Minhaz  165 cm    75   75     50000            Yes
5    Rafi  165 cm    75   72   9000000            Yes
6    Moni  165 cm    75  NaN    250000             No 
'''

new_df = df.replace(to_replace=['#####', '$$$$$', '###'],limit=1, method='ffill')
print(new_df, '\n')
'''
     Name  Height Wight  BPM    Income Dibetic or Not
0   Nahid  165 cm    47   60   6850000             No
1  Hassan  176 cm    46   55     12121            Yes
2    Himu  165 cm    53   80  25000000             No
3    Meem  165 cm    76   75     50000            NaN
4  Minhaz   #####    75   75     50000            Yes
5    Rafi   #####    75   72   9000000            Yes
6    Moni  165 cm    75  NaN    250000             No 
'''
