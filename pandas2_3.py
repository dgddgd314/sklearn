import pandas as pd

stores = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\store_name.csv")
items = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\grocery_item.csv")

items['asset'] = items['price'] * items['count']

items = items.groupby(['store'])['asset'].sum()
items = items.sort_values(ascending=False).head(5)
#print(stores)
print(stores.loc[items.index - 1]['store_name'])