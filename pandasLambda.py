import pandas as pd
import seaborn as sns

def add_10(n):
    return n+10

df = sns.load_dataset('titanic')
print(df['age'].apply(lambda x: add_10(x)))

def mul(a,b):
    try:
        return int(a*b)
    except:
        return 0
    
print(df.apply(lambda x: mul(x['age'], x['survived']), axis = 1))


    