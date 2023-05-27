import pandas as pd

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\population_by_country_2020.csv")
df = df.set_index('Country (or dependency)')
#print(df)
print(df.loc['South Korea'])