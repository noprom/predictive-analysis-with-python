# coding=utf-8
'''
@Title:generate random numbers

@Author: tyee.noprom@qq.com
@Time: 4/21/16 6:34 PM
'''
import numpy as np

# 生成一个随机整数
random_num = np.random.randint(1, 100)
print random_num

# 生成一个0到1的随机小数
random_num = np.random.random()
print random_num


# 生成n个随机数
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


print randint_range(10, 2, 1000)

# shuffle, 随机打算数据
a = range(10)
print a
np.random.shuffle(a)
print a

# choice, 从一个list中随机选择一个元素
print np.random.choice(a)

# 使用随机数种子,每次得到的结果都是一样的
np.random.seed(1)
for i in range(5):
    print np.random.random()
