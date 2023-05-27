import pandas as pd
import seaborn as sns 

df = pd.DataFrame({'ArrivalDate' : ['2020-01-01', '2021-01-01', '2022-01-01'], 'q' : [0,1,2]})
#print(df)
df['year'] = pd.DatetimeIndex(df['ArrivalDate']).year
df['month'] = pd.DatetimeIndex(df['ArrivalDate']).month

