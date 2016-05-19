# coding=utf-8
'''
@Title:

@Author: tyee.noprom@qq.com
@Time: 5/16/16 9:52 PM
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('../data/ch05/Auto.csv')
print data.head()

# 探索建模,是否是线性
data['mpg'] = data['mpg'].dropna()
data['horsepower'] = data['horsepower'].dropna()

plt.plot(data['horsepower'], data['mpg'], 'ro')
plt.xlabel('Horsepower')
plt.ylabel('MPG (Miles Per Gallon)')
plt.show()

# 1.假设一个线性模型mpg = co+a1.horsepower
X = data['horsepower'].fillna(data['horsepower'].mean())
Y = data['mpg'].fillna(data['mpg'].mean())
lm = LinearRegression()
lm.fit(X[:, np.newaxis], Y)
plt.plot(data['horsepower'], data['mpg'], 'ro')
plt.plot(X, lm.predict(X[:, np.newaxis]), color='blue')
plt.show()

# R*R
print lm.score(X[:, np.newaxis], Y)

RSEd = (Y - lm.predict(X[:, np.newaxis])) ** 2
RSE = np.sqrt(np.sum(RSEd) / 389)
ymean = np.mean(Y)
error = RSE / ymean
print RSE, error

# 2.假设非线性模型mpg = co+a1*horsepower^2
X = data['horsepower'].fillna(data['horsepower'].mean()) * data['horsepower'].fillna(data['horsepower'].mean())
Y = data['mpg'].fillna(data['mpg'].mean())
lm = LinearRegression()
lm.fit(X[:, np.newaxis], Y)

# R*R
type(lm.predict(X[:, np.newaxis]))
RSEd = (Y - lm.predict(X[:, np.newaxis])) ** 2
RSE = np.sqrt(np.sum(RSEd) / 390)
ymean = np.mean(Y)
error = RSE / ymean
print RSE, error, ymean

# 3.假设非线性模型mpg = co+a1*horsepower+a2*horsepower^2
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

X = data['horsepower'].fillna(data['horsepower'].mean())
Y = data['mpg'].fillna(data['mpg'].mean())
poly = PolynomialFeatures(degree=2)
X_ = poly.fit_transform(X[:, np.newaxis])
clf = linear_model.LinearRegression()
clf.fit(X_, Y)
print clf.intercept_
print clf.coef_

# 4.假设非线性多阶
X = data['horsepower'].fillna(data['horsepower'].mean())
Y = data['mpg'].fillna(data['mpg'].mean())
poly = PolynomialFeatures(degree=5)
X_ = poly.fit_transform(X[:, np.newaxis])
clf = linear_model.LinearRegression()
clf.fit(X_, Y)
print clf.intercept_
print clf.coef_
