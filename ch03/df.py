# coding=utf-8
'''
@Title:data frame

@Author: tyee.noprom@qq.com
@Time: 4/25/16 7:21 PM
'''
import pandas as pd
import numpy as np

data = pd.DataFrame({'A': np.random.randn(10), 'B': 2.5 * np.random.randn(10) + 1.5})
print data
