import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
from sklearn.datasets._samples_generator import make_blobs

X, y = make_blobs(n_samples=40, centers=2, random_state=20)

clf = svm.SVC(kernel = 'linear') # linear kernel
clf.fit(X, y)

newData = [[3,4]]
print(clf.predict(newData))

plt.scatter(X[:,0], X[:,1], c=y, s=30, cmap=plt.cm.Paired)

# 초평면(Hyper-Plane) 표현
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)
ax.contour(XX, YY, Z, colors='k', levels=[-1,0,1], alpha=0.5, linestyles=['--', '-', '--'])

plt.show()