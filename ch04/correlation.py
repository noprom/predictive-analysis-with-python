# coding=utf-8
'''
@Title:correlation

@Author: tyee.noprom@qq.com
@Time: 5/10/16 9:15 PM
'''
import pandas as pd
import numpy as np

advert = pd.read_csv("../data/ch05/Advertising.csv")
print advert.head()

# find out the correlation between the advertisement costs on TV and the resultant sales.
advert['corrn'] = (advert['TV'] - np.mean(advert['TV'])) * (advert['Sales'] - np.mean(advert['Sales']))
advert['corrd1'] = (advert['TV'] - np.mean(advert['TV'])) ** 2
advert['corrd2'] = (advert['Sales'] - np.mean(advert['Sales'])) ** 2
corrcoeffn = advert.sum()['corrn']
corrcoeffd1 = advert.sum()['corrd1']
corrcoeffd2 = advert.sum()['corrd2']
corrcoeffd = np.sqrt(corrcoeffd1 * corrcoeffd2)
corrcoeff = corrcoeffn / corrcoeffd
print corrcoeff


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
