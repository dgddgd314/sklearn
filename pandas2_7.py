import pandas as pd

# P1
d = {'a':[1,2,3,4,5], 'b':['q','w','e','r','t'], 'c':['q','w','e','r','t']}
left = pd.DataFrame(d)

d = {'a':[2,4,5,6,8], 'd':['q','w','e','r','t'], 'e':['q','w','e','r','t']}
right = pd.DataFrame(d)

print(left.merge(right, on = 'a', how = 'outer'))

# conditional indexing
x = pd.DataFrame({'A':[0,1,2], 'B':[4,5,6]})
print(x.loc[x['A']==2,'B'])
