import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('titanic')
print(df.isnull().sum())

df = df.dropna()  # it erases the NaN, axis = 0
print(df)

df = sns.load_dataset('titanic')
df = df.dropna(axis = 1)  # it erases the vertical line 
print(df)

df = sns.load_dataset('titanic')
print(df.dropna(subset = ['age'], how = 'any', axis = 0))   # dropna method doesn't changes its origin value
print(df)

df = sns.load_dataset('titanic')
df['age'].fillna(df['age'].mean(), inplace = True)  # NaN value transit to the average of df['age'], fillna method changes its origin value
print(df)

df = sns.load_dataset('titanic')
df.replace('S', np.nan, inplace = True)  # replace method doesn't changes its origin value
print(df)
####### seaborn #######
# seaborn is a underneath library of matplotlib.pyplot.