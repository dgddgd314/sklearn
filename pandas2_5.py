import pandas as pd

stores = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\store_name.csv")
items = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\grocery_item.csv")
stores = pd.DataFrame(stores)

items['asset'] = items['price'] * items['count']

items = items.groupby(['store']).sum()
items = items.sort_values(by = ['asset'],ascending=False).head(5)
items = items.join(stores.set_index('store_id'), on = 'store')
items = items.drop(['id','price','count','asset'], axis = 1)
print(items)

