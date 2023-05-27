import pandas as pd
import seaborn as sns

def sum(a,b):
    return a+' '+b

df = sns.load_dataset('tips')
df['day_time'] = df.apply(lambda x: sum(x['day'], x['time']), axis = 1)
print(df[['day_time', 'tip']])

