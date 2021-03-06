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

# Transform data
zscore = lambda x: (x - x.mean()) / x.std()
print grouped.transform(zscore).head(10)

# it can be used to fill the missing values with the mean of the non-missing values
f = lambda x: x.fillna(x.mean())
print grouped.transform(f)

# Miscellaneous operations
print grouped.head(1)
print grouped.tail(1)

# we can use the nth function to get the nth row from a group
grouped = df.groupby('Gender')
print grouped.nth(1)

# Suppose, you want to look at the youngest male and female members of this data frame.
df1 = df.sort_values(['Age', 'Income'])
grouped = df1.groupby('Gender')
grouped.head(1)

# Random sampling – splitting a dataset in training and testing datasets
# Method 1 – using the Customer Churn Model
a = np.random.randn(len(data))
print a
check = a < 0.8
training = data[check]
testing = data[~check]
print 1.0 * len(training) / len(testing)

# Method 2 – using sklearn
from sklearn.cross_validation import train_test_split

train, test = train_test_split(data, test_size=0.2)
print 1.0 * len(train) / len(test)

# Method 3 – using the shuffle function
print("Concatenating and appending data\n")
data1 = pd.read_csv('../data/ch03/winequality-red.csv', sep=';')
print data1.head(10)
print data1.columns.values
print data1.shape

data2 = pd.read_csv('../data/ch03/winequality-white.csv', sep=';')
print data2.head(10)
print data2.columns.values
print data2.shape

# Concat
wine_total = pd.concat([data1, data2], axis=0)
print wine_total.head(10)
print wine_total.shape

data1_head = data1.head(50)
data1_middle = data1[500:550]
data1_tail = data1.tail(50)
wine_scramble = pd.concat([data1_middle, data1_head, data1_tail], axis=0)
print wine_scramble.shape

# 将小文件合并
# 文件太大,下面注释掉
# filepath = "../data/ch03/lotofdata"
# data_final = pd.read_csv(filepath + "/001.csv")
# for i in range(1, 333):
#     if i < 10:
#         filename = '0' + '0' + str(i) + '.csv'
#     if 10 <= i < 100:
#         filename = '0' + str(i) + '.csv'
#     if i >= 100:
#         filename = str(i) + '.csv'
#     file = filepath + '/' + filename
#     data = pd.read_csv(file)
#     data_final = pd.concat([data_final, data], axis=0)
#
# print data_final.tail(1)

# Join and merge operation
# Records
data_main = pd.read_csv("../data/ch03/Medals/Medals.csv")
print data_main.head(10)
# 除重
a = data_main['Athlete'].unique().tolist()
print len(a)
# Country
country_map = pd.read_csv("../data/ch03/Medals/Athelete_Country_Map.csv")
print country_map.head(10)
# Sports
sports_map = pd.read_csv("../data/ch03/Medals/Athelete_Sports_Map.csv")
print sports_map.head(10)

# Merge
# filter first
country_map_dp = country_map.drop_duplicates(subset='Athlete')
merged_dp = pd.merge(left=data_main, right=country_map_dp, left_on='Athlete', right_on='Athlete')
print merged_dp.head()
sports_map_dp = sports_map.drop_duplicates(subset='Athlete')
len(sports_map_dp)
merged_final = pd.merge(left=merged_dp, right=sports_map_dp, left_on='Athlete', right_on='Athlete')
merged_final.head()

# Delete some data
country_map_dlt = country_map_dp[(country_map_dp['Athlete'] <> 'Michael Phelps') &
                                 (country_map_dp['Athlete'] <> 'Natalie Coughlin') &
                                 (country_map_dp['Athlete'] <> 'Chen Jing') &
                                 (country_map_dp['Athlete'] <> 'Richard Thompson') &
                                 (country_map_dp['Athlete'] <> 'Matt Ryan')]
print len(country_map_dlt)

sports_map_dlt = sports_map_dp[(sports_map_dp['Athlete'] <> 'Michael Phelps') &
                               (sports_map_dp['Athlete'] <> 'Natalie Coughlin') &
                               (sports_map_dp['Athlete'] <> 'Chen Jing') &
                               (sports_map_dp['Athlete'] <> 'Richard Thompson') &
                               (sports_map_dp['Athlete'] <> 'Matt Ryan')]
print len(sports_map_dlt)

data_main_dlt = data_main[(data_main['Athlete'] <> 'Michael Phelps') &
                          (data_main['Athlete'] <> 'Natalie Coughlin') &
                          (data_main['Athlete'] <> 'Chen Jing') &
                          (data_main['Athlete'] <> 'Richard Thompson') &
                          (data_main['Athlete'] <> 'Matt Ryan')]
print len(data_main_dlt)

# Left join demo
merged_inner = pd.merge(left=data_main, right=country_map_dlt, how='inner', left_on='Athlete', right_on='Athlete')
print len(merged_inner)

# Right join demo
merged_right = pd.merge(left=data_main_dlt, right=country_map_dp, how='right', left_on='Athlete', right_on='Athlete')
print len(merged_right)
