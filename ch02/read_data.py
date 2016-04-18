# coding=utf-8
'''
@Title:read data from a csv file

@Author: tyee.noprom@qq.com
@Time: 4/16/16 6:52 PM
'''
import pandas as pd
import os
# 使用 open 函数来打开
data = open('../data/ch02/Customer Churn Model.txt', 'r')
cols = data.next().strip().split(',')
no_cols = len(cols)
print(cols)
print(no_cols)

# 使用read_csv读取文件内容
path = '../data/ch02'                   # 从csv文件读取数据
filename = 'titanic3.csv'
fullpath = os.path.join(path,filename)
data = pd.read_csv(fullpath)            # 读取数据
print data.describe()                   # 描述数据
print data.columns.values               # 打印表头
print data.dtypes                       # 打印数据的类型
print pd.isnull(data['body'])           # 打印body这一列是否为null
print pd.isnull(data['body']).values.ravel().sum()  # 打印为null的个数
print data['body']                      # 打印body这一列
print data['body'].fillna(0)            # 将NaN替换为0
print data['age'].fillna(data['age'].mean()) # 用平均数替换NaN
print data['age'].fillna(method='ffill') # 使用前面最近的来替换
print data['age'].fillna(method='backfill') # 使用后面最近的来替换

# 将性别分别转化为0和1
dummy_sex = pd.get_dummies(data=data['sex'], prefix='sex')
print dummy_sex
