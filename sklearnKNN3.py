import seaborn as sns
import matplotlib.pyplot as plt

####### data preparation #######

df = sns.load_dataset('penguins')
df = df.drop(columns = ['island','bill_length_mm','bill_depth_mm','sex'])
df = df.dropna(axis = 0)

####### data ploting #######

sns.lmplot(x = 'flipper_length_mm', y = 'body_mass_g', data = df,
           fit_reg=False, # show data regression
           scatter_kws={'s':50},
           hue= 'species'
           )
plt.show()

####### data divide #######
from sklearn.model_selection import train_test_split
train, test = train_test_split(df, train_size=0.8)
x_train, y_train = train[['flipper_length_mm', 'body_mass_g']], train['species']
x_test, y_test = test[['flipper_length_mm', 'body_mass_g']], test['species']

###### finding k ########

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
k_list = list(range(1, 30))
score = []
for k in k_list:
    knn = KNeighborsClassifier(k)
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    score.append(accuracy_score(pred, y_test))
    
print(score)
k = k_list[score.index(max(score))]
print(k)

      
    