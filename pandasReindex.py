import pandas as pd

li = [[1]*3 for _ in range(3)]
df = pd.DataFrame(li, index = ['0','1','2'])

# df.iloc can change the data, with only the spot
# df.loc can change the data, but with the name of the index
df.iloc[0][1] = 8
df.loc['1'][2] = 9

#print(df)
# df.reindex can change the data using new index
print(df)
df = df.reindex(['2','1','0'])
print(df)