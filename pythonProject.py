# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 17:13:20 2014

@author: Braden
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib import request


filename = "results2.csv"

#Reads csv file into dataframe
df = pd.read_csv(filename, encoding='latin1')

#Drops any rows that do not contain any information in them
df2 = df.dropna(how='any')

mean = df.mean()

#Display Averages of the Data for insight
print ('The averages of the data: \n', np.round(df.mean(), decimals=2))

df['SaleDate'] = df['SaleDate'].map(lambda x: str(x)[6:])

df.SaleDate

