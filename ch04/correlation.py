# coding=utf-8
'''
@Title:correlation

@Author: tyee.noprom@qq.com
@Time: 5/10/16 9:15 PM
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

advert = pd.read_csv("../data/ch05/Advertising.csv")
print advert.head()


# find out the correlation between the advertisement costs on TV and the resultant sales.

# Calculate correlation func
def corrcoeff(df, var1, var2):
    df['corrn'] = (df[var1] - np.mean(df[var1])) * (df[var2] - np.mean(df[var2]))
    df['corrd1'] = (df[var1] - np.mean(df[var1])) ** 2
    df['corrd2'] = (df[var2] - np.mean(df[var2])) ** 2
    corrcoeffn = df.sum()['corrn']
    corrcoeffd1 = df.sum()['corrd1']
    corrcoeffd2 = df.sum()['corrd2']
    corrcoeffd = np.sqrt(corrcoeffd1 * corrcoeffd2)
    corrcoeff = corrcoeffn / corrcoeffd
    return corrcoeff


corrcoeff_val = corrcoeff(advert, 'TV', 'Sales')
print corrcoeff_val
# draw the relationship between TV and Sales
plt.plot(advert['TV'], advert['Sales'], 'ro')
plt.title('TV vs Sales')
plt.show()
