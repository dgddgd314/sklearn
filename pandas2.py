import pandas as pd

li = [['M',13],['M',16],['F',15]]
df = pd.DataFrame(li)

df.index = ['Bob','John','Bell']
df.columns = ['gender','age']

# print(df)
df.rename(index = {"Bob":"Spongebob"}, columns = {"age":"나이"}, inplace = True) #bool inplace is False
print(df.loc['Bob',:])

