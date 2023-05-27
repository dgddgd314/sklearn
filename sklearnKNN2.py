import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.3, random_state=10)
#print(x_train.shape)
#print(y_train.shape)

from sklearn.neighbors import KNeighborsClassifier
k_range = range(1,26)
score_list = []

from sklearn.model_selection import cross_val_score

for k in k_range:
    knn = KNeighborsClassifier(k)
    score = cross_val_score(knn,x_train, y_train, cv = 7)
    score_list.append(score.mean())
    
pd.Series(score_list, k_range).plot()
k = k_range[score_list.index(max(score_list))]
print(score_list, k)
#plt.show()

knn = KNeighborsClassifier(k)
knn.fit(x_train, y_train)
pred = knn.predict(x_test)

from sklearn.metrics import accuracy_score
print("R_square : ",accuracy_score(pred, y_test))

# Another example?