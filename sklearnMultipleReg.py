import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips')
ndf = df[['total_bill','tip','size']]

x = ndf[['total_bill', 'size']]
y = ndf['tip']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)

print(lr.score(x_test, y_test))
print(lr.coef_)   # ['total_bill', 'size']
print(lr.intercept_)   # bias