# coding=utf-8
'''
@Title:read data from a csv file

@Author: tyee.noprom@qq.com
@Time: 4/16/16 6:52 PM
'''
import pandas as pd
import os
path = '../data/ch02'                   # 从csv文件读取数据
filename = 'titanic3.csv'
fullpath = os.path.join(path,filename)
data = pd.read_csv(fullpath)            # 读取数据
print data.describe()
print data.columns.values              # 打印表头

# 使用 open 函数来打开
data = open('../data/ch02/Customer Churn Model.txt', 'r')
cols = data.next().strip().split(',')
no_cols = len(cols)
print(cols)
print(no_cols)