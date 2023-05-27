import pandas as pd

emp = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\employees.csv")
dep = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\departments.csv")

# print(emp)
df = emp.groupby('DEPARTMENT_ID')['SALARY'].mean()
df = df.sort_values(ascending=False).head(1)

dpt_id = df.index[0]
emp_id = dep.loc[dep['DEPARTMENT_ID'] == dpt_id]['MANAGER_ID']
#print(emp_id)

print(emp.loc[emp['EMPLOYEE_ID']==int(emp_id)]['FIRST_NAME'])