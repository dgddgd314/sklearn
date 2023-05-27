import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\basketball_stat.csv")
df = df.drop(['2P', 'AST', 'STL'], axis = 1)

####### divide test and training data #######

from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size = 0.2)

x_train, y_train = train[['3P', 'BLK', 'TRB']], train['Pos']
x_test, y_test = test[['3P', 'BLK', 'TRB']], test['Pos']

####### SVM #######

from sklearn import svm
svm_model = svm.SVC() # creates model
svm_model.fit(x_train, y_train)
pred = svm_model.predict(x_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, pred))