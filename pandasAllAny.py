import pandas as pd
import numpy as np

print(pd.Series([True, True, True,True]).all())
print(pd.Series([True, False, True, True]).all())
print(pd.Series([False, False, False]).all())


print(pd.Series([True, True, True,True]).any())
print(pd.Series([True, False, True, True]).any())
print(pd.Series([False, False, False]).any())

print(pd.Series([np.nan]).all())    # T
print(pd.Series([np.nan]).all(skipna = False))   # T

print(pd.Series([np.nan]).any(skipna = False))    # T
print(pd.Series([np.nan]).any(skipna = True))     # F
