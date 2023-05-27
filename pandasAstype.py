import pandas as pd

df = pd.DataFrame([[1.1,2,3],[4,5.0,6]], columns=["A","B","C"])
print(df)
print(df.astype('int'))
print(df.astype({"A":'int', "B":'complex'}))    # B : x + yj

sr = pd.DataFrame([1,2,3,'4',5])
print(sr.astype('float16'))
print(sr.astype('string'))

######## category ####### (levels in R)

sr = pd.DataFrame(["a","b","c","a"], dtype='category')
print(sr)

# category is like gender or city.
# it can't add.


