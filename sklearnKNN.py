import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\basketball_stat.csv")
'''sns.lmplot(x = 'BLK', y = '3P', data = df, 
           fit_reg =False,  # do not make regression line
           scatter_kws={'s':100}, # it sends data to pyplot 
           markers=['o','x'],
           hue = 'Pos') '''

df = df.drop(['2P', 'AST', 'STL'], axis = 1)

####### divide test and training data #######

from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size = 0.2)

x_train, y_train = train[['3P', 'BLK', 'TRB']], train['Pos']
x_test, y_test = test[['3P', 'BLK', 'TRB']], test['Pos']

####### finding best k, inside the training set #######

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

k_list = list(range(3, train.shape[0]//2,2))
cross_scores = []
for k in k_list:
    knn = KNeighborsClassifier(k)
    scores = cross_val_score(knn, x_train, y_train, cv = 10)
    cross_scores.append(scores.mean())
print(cross_scores)
pd.Series(cross_scores, k_list).plot()

plt.show()

k = k_list[cross_scores.index(max(cross_scores))]

####### apply best k to the test sample #######

knn = KNeighborsClassifier(k)
knn.fit(x_train, y_train)
pred = knn.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))
