import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\SBUX.csv")
print(df)

df['Month'] = pd.DatetimeIndex(df['Date']).month
df['Year'] = pd.DatetimeIndex(df['Date']).year

df.groupby(['Year','Month'])['Close'].mean().plot()

plt.show()
