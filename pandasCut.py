import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

ages = [0,20,40,60,80]
category = ['kid', 'young', 'middle', 'old']

df['age_range'] = pd.cut(x = df['age'], bins = ages, labels = category)

######## cut ########
# pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True)
# x is the data that is reference
# bins is list or int. if it is list, it divides it by that value. if it is int, it divides data to the number of int value

print(df[['age', 'age_range']].head(10))