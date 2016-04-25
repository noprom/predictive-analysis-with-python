# coding=utf-8
'''
@Title:calculate the value of pi

@Author: tyee.noprom@qq.com
@Time: 4/25/16 6:36 PM
'''
import numpy as np
import matplotlib.pyplot as plt

pi_avg = 0
pi_value_list = []
for i in range(100):
    value = 0
    x = np.random.uniform(0, 1, 1000).tolist()
    y = np.random.uniform(0, 1, 1000).tolist()
    for j in range(1000):
            z = np.sqrt(x[j] * x[j] + y[j] * y[j])
            if z <= 1:
                value += 1
    float_value = float(value)
    pi_value = float_value * 4 / 1000
    pi_value_list.append(pi_value)
    pi_avg += pi_value
pi = pi_avg / 100
print pi
ind = range(1,101)
fig = plt.plot(ind,pi_value_list)
plt.show()
