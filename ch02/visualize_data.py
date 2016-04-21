# coding=utf-8
'''
@Title:visualize_data

@Author: tyee.noprom@qq.com
@Time: 4/18/16 8:07 PM
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/ch02/Customer Churn Model.txt')
# 画一个scatter图,显示4张小图,2x2
figure, axs = plt.subplots(2, 2, sharey=True, sharex=True)
data.plot(kind='scatter', x='Day Mins', y='Day Charge', ax=axs[0][0])
data.plot(kind='scatter', x='Night Mins', y='Night Charge', ax=axs[0][1])
data.plot(kind='scatter', x='Day Calls', y='Day Charge', ax=axs[1][0])
data.plot(kind='scatter', x='Night Calls', y='Night Charge', ax=axs[1][1])
plt.show()

# 画一个histogram图
plt.hist(data['Day Calls'],bins=8)
plt.xlabel('Day Calls Value')               # x坐标显示的文字
plt.ylabel('Frequency')                     # y坐标显示的文字
plt.title('Frequency of Day Calls')         # 整张图的标题
plt.show()

# 画一个boxplot图
plt.boxplot(data['Day Calls'])
plt.ylabel('Day Calls')
plt.title('Box Plot of Day Calls')
plt.show()

# 生成正态分布的随机数,并且显示
x = range(1, 101)
y = np.random.uniform(1, 100, 100)
plt.hist(y)
plt.show()
