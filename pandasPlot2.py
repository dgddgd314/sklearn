import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\employees.csv")
print(emp)

emp.groupby("JOB_ID").size().plot(kind = "bar")
plt.show()