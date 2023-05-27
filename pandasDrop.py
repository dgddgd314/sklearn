import pandas as pd

# set dataframe with dict
df = pd.DataFrame({'company' : ['AAPL', 'MSFT', 'GOOG'], 'price' : ['180','340','2900'], 'cap' : ['2900B', '2600B', '2000B']})
# print(df)   

# add new index with df.loc method
df.loc[3] = ['TSLA', '1000', '1000B']

# add new column with df['_']
df['rank'] = [1,2,3,4]

# set index as company, return exist
df = df.set_index('company')
# print(df)

# change index with column
df = df.transpose()
# print(df)

# drop => choose index or columns, bool inplace is False
df.drop(index = 'rank', inplace = True)
df.drop(columns = 'MSFT', inplace = True)

print(df)