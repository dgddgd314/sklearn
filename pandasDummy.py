import pandas as pd
import seaborn as sns 

df = sns.load_dataset('titanic')
dummy = pd.get_dummies(df['sex'])

print(df['sex'].head(3))
print(dummy.head(3))
