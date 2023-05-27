import pandas as pd

data = {'Animal' : ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 'Max Speed' : [380, 370, 24,26]}
df = pd.DataFrame(data)

print(df)
print()

# unite data with name, take the data with mean()
mean_data = df.groupby(['Animal']).mean()
print(mean_data)
