import pandas as pd

left = pd.DataFrame({'key':[1,2,3], 'name':['A', 'B', 'C']})
right = pd.DataFrame({'key':[2,3,1], 'age':[18,15,20]})

joined_df = left.merge(right, on = 'key')

# joined_df = left.merge(right, left_on = 'key', right_on = 'key')

d = {'id': [3,6,9],'name':['a','b','c']}
left = pd.DataFrame(d)

d = {'name':['a','b','d'], 'country':['KOR','USA','ENG']}
right = pd.DataFrame(d)

print(left.merge(right, on='name', how = 'inner'))
print(left.merge(right, on='name', how = 'outer'))
print(left.merge(right, on='name', how = 'left'))
print(left.merge(right, on='name', how = 'right'))