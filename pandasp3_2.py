import pandas as pd
import numpy as np

dpt = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\departments.csv")
emp = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\employees.csv")

dpt = dpt.replace(" - ", np.nan)
dpt['MANAGER_ID'] = pd.to_numeric(dpt['MANAGER_ID'])

df = dpt.merge(emp, left_on='MANAGER_ID', right_on='EMPLOYEE_ID')
df = df.dropna()
print(df[['FIRST_NAME','DEPARTMENT_NAME']])
