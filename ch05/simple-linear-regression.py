# coding=utf-8
'''
@Title:simple-linear-regression

@Author: tyee.noprom@qq.com
@Time: 5/16/16 7:54 PM
'''

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

advert = pd.read_csv('../data/ch05/Advertising.csv')
feature_cols = ['TV', 'Radio']


def predict():
    '''
    预测
    [('TV', 0.046263139747618941), ('Radio', 0.18675148241866898)]
    intercept = 2.81251458876
    R*R = 0.885772762525
    :return:
    '''
    X = advert[feature_cols]
    Y = advert['Sales']
    trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.2)
    lm = LinearRegression()
    lm.fit(trainX, trainY)

    # print lm.intercept_
    # print lm.coef_
    # print zip(feature_cols, lm.coef_)
    # R*R
    # print lm.score(trainX, trainY)
    # Predict
    predY = lm.predict(testX)
    print predY


def error_ratio():
    '''
    计算错误率
    :return:
    '''
    # advert['RSE'] = (advert['Sales'] - advert['sales_pred']) ** 2
    # RSEd = advert.sum()['RSE']
    # RSE = np.sqrt(RSEd / 51)
    # salesmean = np.mean(advert['Sales'])
    # error = RSE / salesmean
    # RSE, salesmean, error


def feature_select():
    '''
    Feature selection
    :return:
    '''
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


# =====================主程序开始===================== #
predict()
error_ratio()