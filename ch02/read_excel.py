# coding=utf-8
'''
@Title:read_excel

@Author: tyee.noprom@qq.com
@Time: 4/18/16 7:16 PM
'''
import pandas as pd
data = pd.read_excel(io='../data/ch02/titanic3.xls', sheetname='titanic3') # 第二个参数是需要读入的sheet名称
print data.head()

