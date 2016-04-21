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


def randint_range(n, a, b):
    '''
    生成n个a~b之间的随机数
    :param n: 随机数个数
    :param a: 最小值
    :param b: 最大值
    :return: 随机数list
    '''
    x = []
    for i in range(n):
        x.append(np.random.randint(a, b))
    return x
