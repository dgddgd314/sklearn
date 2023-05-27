import pandas as pd

dpt = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\departments.csv")
emp = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\employees.csv")

df = dpt.groupby('DEPARTMENT_NAME').size()
print(df)