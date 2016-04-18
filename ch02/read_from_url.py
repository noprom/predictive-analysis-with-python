# coding=utf-8
'''
@Title:read_from_url

@Author: tyee.noprom@qq.com
@Time: 4/18/16 7:11 PM
'''
import csv
import urllib2
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = urllib2.urlopen(url)
cr = csv.reader(response)
for rows in cr:
    print rows