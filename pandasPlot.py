import pandas as pd
import matplotlib.pyplot as plt

coun = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\population_by_country_2020.csv")
fig1 = coun.set_index("Country (or dependency)").sort_values("Density (P/Km²)", ascending=False)["Density (P/Km²)"].head(10).plot(kind = "bar")

plt.show()
