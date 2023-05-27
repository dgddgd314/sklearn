import pandas as pd
import random

random.seed(0)
li = [[random.randint(1,100) for _ in range(5)] for _ in range(5)]
df = pd.DataFrame(li)

# P1
'''df.set_index([0,4], inplace = True)
print(df)'''

# P2
'''df = df.reindex([1,2,4,8])
print(df)'''

# P3
'''df.sort_values(by=1, ascending = True, inplace = True)
print(df)'''
