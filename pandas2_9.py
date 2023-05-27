import pandas as pd

# it counts
sr = pd.Series([5,3,7,2,8,3,5,54,4,2,2,5,2])
print(sr.value_counts())

df = pd.DataFrame({'name':['David', 'Ben', 'Homer', 'Cole', 'Lee', 'Kim', 'Choi'], 'company':['a','b','c','b','c','b','b']})

print(df)
print()
# first grouping, next count
#print(df.groupby('company').count())

# first grouping, next sizing
print(df.groupby('company').size())
