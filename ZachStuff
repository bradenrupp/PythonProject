import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib import request
from datetime import datetime
#from pandas.tools.plotting import lag_plot

filename = "results2.csv"

df = pd.read_csv(filename, encoding='latin1')

'''
#Year built
format = "%Y"
times = pd.to_datetime(df.Yr, format=format)
df.set_index(times, inplace=True)
#df = df.drop(['Yr'], axis=1)
'''
#Change Sale Date to int
df['SaleDate'] = df['SaleDate'].map(lambda x: str(x)[6:])
df['SaleDate'] = df['SaleDate'].astype(int)

#Sale date
format = "%Y"
times = pd.to_datetime(df.SaleDate, format=format)
df.set_index(times, inplace=True)

'''
#plots
df.plot(kind='scatter', x='Yr', y='Price');
df.plot(kind='line', x='Yr', y='Price');
df.plot(kind='scatter', x='Bath (1/2 + full)', y='Price');
df.plot(kind='scatter', x='TBr', y='Price');
'''

'''
#Other plots
df.plot()
df.Price.plot()
'''
