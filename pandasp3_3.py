import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
# print(df)
li = [2700, 3900, 5100, 6300]
value = ['small', 'medium', 'big']

df['size'] = pd.cut(x = df['body_mass_g'], bins = li, labels = value)
print(df)

print(df.groupby('size').size())

# if value is smaller than 2700 or bigger than 6300, it becomes NaN