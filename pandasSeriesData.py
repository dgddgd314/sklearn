import pandas as pd
import seaborn as sns

df = sns.load_dataset('taxis')
print(df.info())
df = df[['pickup', 'dropoff']]

df['pickup'] = pd.to_datetime(df['pickup'])
print(df.info())
# to_datetime changes dtype to datetime object.

timestamp = pd.to_datetime(list(df['pickup']))
print(timestamp[:3],'\n')

day_period = timestamp.to_period(freq = 'D')
print(day_period[:3])

#there are some more freq options
# D, W, MS, M, AS, A, B, H, QS, Q, T, S

####### date_range #######
ts = pd.date_range(start = '2021-01-02', end = '2021-04-05', freq = 'MS')
print(ts, '\n')

ts = pd.date_range(start = '2021-01-02', periods=3, freq = 'MS')
print(ts)

ts2 = pd.date_range(start = '2021-01-02', periods=3, freq = '3MS')
print(ts2)