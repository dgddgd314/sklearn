import pandas as pd

def add_5(n):
    return n+5

def add_num(a,b):
    return a+b

df = pd.DataFrame({'a':[1,2,3], 'b':[1,2,3], 'c':[1,2,3]})
df['a'] = df['a'].apply(add_5)
print(df)

df['a'] = df['a'].apply(add_num, b = 10) # parameters comes later
print(df)

df = df.applymap(add_num, b = -5)   # it applys the whole Dataframe
print(df)