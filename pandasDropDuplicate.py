from re import sub
import pandas as pd

df = pd.DataFrame([[1,1,3,4],[1,3,4,5],[1,1,3,4],[4,5,3,4]])
print(df)

df = df.drop_duplicates()  # it erases the first one
print(df)

df = df.drop_duplicates(subset=[0])   # if first column is same, erases it.
print(df)