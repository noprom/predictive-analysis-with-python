# coding=utf-8
'''
@Title:read data from a csv file

@Author: tyee.noprom@qq.com
@Time: 4/16/16 6:52 PM
'''
import pandas as pd
import numpy as np
import os

# 使用 open 函数来打开
data = open('../data/ch02/Customer Churn Model.txt', 'r')
cols = data.next().strip().split(',')
no_cols = len(cols)
print(cols)
print(no_cols)

# 使用read_csv读取文件内容
path = '../data/ch02'  # 从csv文件读取数据
filename = 'titanic3.csv'
fullpath = os.path.join(path, filename)
data = pd.read_csv(fullpath)  # 读取数据
print data.describe()  # 描述数据
print data.columns.values  # 打印表头
print data.dtypes  # 打印数据的类型
print pd.isnull(data['body'])  # 打印body这一列是否为null
print pd.isnull(data['body']).values.ravel().sum()  # 打印为null的个数
print data['body']  # 打印body这一列
print data['body'].fillna(0)  # 将NaN替换为0
print data['age'].fillna(data['age'].mean())  # 用平均数替换NaN
print data['age'].fillna(method='ffill')  # 使用前面最近的来替换
print data['age'].fillna(method='backfill')  # 使用后面最近的来替换

# 将性别分别转化为0和1
dummy_sex = pd.get_dummies(data=data['sex'], prefix='sex')
print dummy_sex
# 将性别那一列用数字替换
column_name = data.columns.values.tolist()
column_name.remove('sex')
data = data[column_name].join(dummy_sex)
print data.head(5)

# 使用data frame
data = pd.DataFrame({'A': np.random.randn(10), 'B': 2.5 * np.random.randn(10) + 1.5}, index=range(10, 20))
print data

# Group data

a = ['Male', 'Female']
b = ['Rich', 'Poor', 'Middle Class']
gender = []
seb = []
for i in range(1, 101):
    gender.append(np.random.choice(a))
    seb.append(np.random.choice(b))
height = 30 * np.random.randn(100) + 155
weight = 20 * np.random.randn(100) + 60
age = 10 * np.random.randn(100) + 35
income = 1500 * np.random.randn(100) + 15000
df = pd.DataFrame({'Gender': gender, 'Height': height, 'Weight': weight, 'Age': age,
                   'Income': income, 'Socio-Eco': seb})
print df.head()

# group data
grouped = df.groupby('Gender')
print grouped.groups
for names, groups in grouped:
    print names
    print groups
# 筛选其中的group
print grouped.get_group('Female')

# 多个字段group
grouped = df.groupby(['Gender', 'Socio-Eco'])
for names, groups in grouped:
    print names
    print groups

# Aggregation data
print grouped.sum()
print grouped.size()
print grouped.describe()
grouped_income = grouped['Income']
print grouped_income
# customize aggregation
print grouped.aggregate({'Income': np.sum, 'Age': np.mean, 'Height': np.std})
# use lambda
print grouped.aggregate({'Age': np.mean, 'Height': lambda x: np.mean(x) / np.std(x)})
# apply several functions to all the columns at the same time
print grouped.aggregate([np.sum, np.mean, np.std])

# Filter data
print grouped['Age'].filter(lambda x: x.sum() > 700)
