# coding=utf-8
'''
@Title:simple-linear-regression

@Author: tyee.noprom@qq.com
@Time: 5/16/16 7:54 PM
'''

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

advert = pd.read_csv('../data/ch05/Advertising.csv')
feature_cols = ['TV', 'Radio']
X = advert[feature_cols]
Y = advert['Sales']
trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.2)
lm = LinearRegression()
lm.fit(trainX, trainY)

print lm.intercept_
print lm.coef_
print zip(feature_cols, lm.coef_)
# R*R
print lm.score(trainX, trainY)
# Predict
print lm.predict(testX)

# Feature selection
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

feature_cols = ['TV', 'Radio', 'Newspaper']
X = advert[feature_cols]
Y = advert['Sales']
estimator = SVR(kernel="linear")
selector = RFE(estimator, 2, step=1)
selector = selector.fit(X, Y)
print selector.support_
print selector.ranking_