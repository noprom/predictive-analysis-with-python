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

