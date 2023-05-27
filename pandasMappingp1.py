import pandas as pd
import seaborn as sns

def exchange(dollar):
    return dollar*1200

df = sns.load_dataset('tips')
df['total_bill'] = df['total_bill'].apply(exchange)
df['tip'] = df['tip'].apply(exchange)
print(df[['total_bill', 'tip']])