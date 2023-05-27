import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("C:\\Users\\82103\\Downloads\\data\\weight_height.csv")

x = df[['Height']]  # independent variable must be double
y = df['Weight']  # dependent variable must be single

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = (train_test_split(x, y, test_size=0.3, random_state=10))

poly = PolynomialFeatures(degree = 6)
x_train_poly = poly.fit_transform(x_train)

print(x_train.shape, x_train_poly.shape)  # 1, x, x**2

lr = LinearRegression()
lr.fit(x_train_poly, y_train)

x_test_poly = poly.fit_transform(x_test)
r_square = lr.score(x_test_poly, y_test)
print(r_square) # https://blog.naver.com/dragon5384/222833934383


# how can I find the coefficient?
print(lr.coef_)
print(lr.intercept_)
