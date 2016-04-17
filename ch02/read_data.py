# coding=utf-8
'''
@Title:read data from a csv file

@Author: tyee.noprom@qq.com
@Time: 4/16/16 6:52 PM
'''
import pandas as pd
data = pd.read_csv('../data/ch02/titanic3.csv') # 从csv文件读取数据
print(data.head())