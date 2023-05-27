import pandas as pd
import numpy as np
import math

li = ['1', '2', 3]
sr1 = pd.to_numeric(li, errors = 'raise') # raise, coerce, ignore 
print(sr1)

df = pd.DataFrame([[0,1,'2'],[3,'4',5.0]])
#print(pd.to_numeric(df)) # error!
print(df.apply(pd.to_numeric))  

####### apply #######
df = pd.DataFrame([[4,9] for _ in range (3)])
print(df)
#print(df.apply(math.sqrt))  # error! => apply gives series to the function
print(df.apply(np.sqrt))   # numpy can get series, and return it!
