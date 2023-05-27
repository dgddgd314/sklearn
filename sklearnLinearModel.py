import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\weight_height.csv")

x = df[['Height']]  # independent variable must be double
y = df['Weight']  # dependent variable must be single

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = (train_test_split(x, y, test_size=0.3, random_state=10))

print(len(x_train), len(x_test))

from sklearn.linear_model import LinearRegression

# making object
lr = LinearRegression()

lr.fit(x_train, y_train)  # learning!

r_square = lr.score(x_test, y_test)
print("R**2 :", r_square)
print("m :", lr.coef_)
print("bias :", lr.intercept_)

y_hat = lr.predict(x)
ax1 = sns.kdeplot(y, color = 'b')   # it shows overall distribution of data
ax2 = sns.kdeplot(y_hat, color = 'r')

plt.show()