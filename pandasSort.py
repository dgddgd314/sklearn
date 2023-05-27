import pandas as pd
import numpy as np

df = pd.DataFrame({'class' : ['birds','birds','mammal','mammal'], 'max_speed' : [389.0, 24.0, 80.5,np.nan]}, index = ['falcon', 'parrot', 'lion', 'monkey'])
#print(df)

# reset_index resets index and adds it on columns.
# if you don't want to add it, you can use the parameters; drop
df = df.reset_index(drop = False)
# print(df)

# sort_values can sort df by data using 'by' parameters
# if you want to sort on reverse, use parameters; ascending. bool is True
df = df.sort_values(by = ['max_speed'], ascending = True)
print(df)


df = df.set_index('index')
# sort_index can sort df by index
# if you want to sort on reverse, use parameters; ascending. bool is True
df = df.sort_index(ascending = True)
print(df)

