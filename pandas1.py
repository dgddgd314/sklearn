import pandas as pd
import numpy as np

li = ['a','b','c','d']

s = pd.Series(li)
print(s)

dic = {'철수':175, '영수':169, '희진':172, '이름':'키'}

s = pd.Series(dic)
print(s)

tu = ('a', 'e', 'l', 'p')

s = pd.Series(tu)
li = list(s)
#ar = np.array(li)
#print(ar.ndim)
print(s[[0,3,3,2,1]])

monthday = ('day',31,28,31,30,31,30,31,31,30,31,30,31)

s = pd.Series(monthday, index = ['month'] + list(range(1,13)))
print(s)