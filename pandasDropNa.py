import pandas as pd
import numpy as np

dpt = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\departments.csv")
print(dpt)

dpt = dpt.replace(" - ", np.nan)
dpt = dpt.dropna(subset = ["MANAGER_ID"], axis = 0)

print(dpt)
