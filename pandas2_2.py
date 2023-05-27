import pandas as pd

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\grocery_item.csv")
mean_data = df.groupby(['store'])['price'].min() # grammar, combine which is same store. Show minimum price only
print(mean_data.sort_values().head(5))

# this is also good
'''mean_data = mean_data.reset_index()
mean_data = mean_data.sort_values(by = 'price')
mean_data = mean_data.set_index('price')
mean_data = mean_data.sort_index()
data = mean_data.iloc[0:5,0:1]
data = data.reset_index()
data = data.set_index('store')
print(data)'''