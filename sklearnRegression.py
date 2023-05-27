import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\weight_height.csv")
#df.plot(x = 'Height', y = 'Weight', kind = 'scatter')
sns.regplot(x = 'Height', y = 'Weight', data = df, line_kws={'color':'g'})  # draws regression line

plt.show()

x = df[['Height']]  # independent variable must be double
y = df['Weight']  # dependent variable must be single

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = (train_test_split(x, y, test_size=0.3, random_state=10))

print(len(x_train), len(x_test))

