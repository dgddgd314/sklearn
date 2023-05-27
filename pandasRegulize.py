import pandas as pd
import seaborn as sns

df = sns.load_dataset("diamonds")
print(df['price'].head())
print()

df['price'] = df['price'] / abs(df['price'].max())
print(df['price'])

# every value is between 1 to -1