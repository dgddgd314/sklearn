import pandas as pd

left = pd.DataFrame({'key':[1,2,3], 'name':['A','B','C']})
right = pd.DataFrame({'key':[2,3,1], 'age':[15,20,39]})

# joined_df = left.join(right, lsuffix='_ ')

# 1
joined_df = left.set_index('key').join(right.set_index('key'))

# 2
joined_df = left.join(right.set_index('key'), on = 'key')

print(joined_df)