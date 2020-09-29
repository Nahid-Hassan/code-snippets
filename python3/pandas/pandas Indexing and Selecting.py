#The callable must be a function with one argument (the calling Series,
# DataFrame or Panel and that returns valid output for indexing)
#Data 16-04-2019 Time: 4:50

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,4),index = list('abcdef'), columns=list('ABCD'))
print(df,'\n')
print(df.A,'\n')

print(df.loc[lambda df: df.A > 0,:])
print(df.loc[:,lambda df: ['A','C']])
print(df.iloc[:,lambda df:[0,3]])

#this simple pandas indexing and selecting program