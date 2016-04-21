# coding=utf-8
'''
@Title:generate random numbers

@Author: tyee.noprom@qq.com
@Time: 4/21/16 6:34 PM
'''
import numpy as np

# 生成一个随机整数
random = np.random.randint(1, 100)
print random

# 生成一个0到1的随机小数
random = np.random.random()
print random
