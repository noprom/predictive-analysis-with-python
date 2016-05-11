# coding=utf-8
'''
@Title:Linear regression

@Author: tyee.noprom@qq.com
@Time: 5/10/16 10:15 PM
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = 2.5 * np.random.randn(100) + 1.5
res = .5 * np.random.randn(100) + 0
ypred = 2 + .3 * x
yact = 2 + .3 * x + res
xlist = x.tolist()
ypredlist = ypred.tolist()
yactlist = yact.tolist()
df = pd.DataFrame({'Input_Variable(X)': xlist, 'Predicted_Output(ypred)': ypredlist, 'Actual_Output(yact)': yactlist})
print df.head()

# plot the predicted and actual data
x = 2.5 * np.random.randn(100) + 1.5
res = .5 * np.random.randn(100) + 0
ypred = 2 + .3 * x
yact = 2 + .3 * x + res
ymean = np.mean(yact)
yavg = [ymean for i in range(1, len(xlist) + 1)]
plt.plot(x, ypred)
plt.plot(x, yact, 'ro')
plt.plot(x, yavg)
plt.title('Actual vs Predicted')
plt.show()

# calculate RR
df['SSR'] = (df['Predicted_Output(ypred)'] - ymean) ** 2
df['SST'] = (df['Actual_Output(yact)'] - ymean) ** 2
SSR = df.sum()['SSR']
SST = df.sum()['SST']
print SSR / SST
