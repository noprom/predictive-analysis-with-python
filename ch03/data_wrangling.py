# coding=utf-8
'''
@Title:data_wrangling

@Author: tyee.noprom@qq.com
@Time: 4/18/16 9:02 PM
'''
import pandas as pd

data = pd.read_csv('../data/ch02/Customer Churn Model.txt')
account_length = data['Account Length']  # 选择一列
print account_length.head()
print type(account_length)

subdata = data[['Account Length', 'VMail Message', 'Day Calls']]  # 选择多列
print subdata.head()
print type(subdata)

# 另外一种选择多个子列的方式
wanted_columns = ['Account Length', 'VMail Message', 'Day Calls']
subdata = data[wanted_columns]
print subdata.head()
