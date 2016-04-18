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

subdata = data[['Account Length', 'VMail Message', 'Day Calls']]    # 选择多列
print subdata.head()
