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

low_memory=False

filename = "results.csv"
filename2 = "results2.csv"
#df = pd.read_csv(filename, encoding='latin1')\
df2 = pd.read_csv(filename2, encoding='latin1')



#print(df.iloc[1])

#print(df.iloc[44])

#print(df.iloc[44][3])

test = str(df.iloc[44][3])


if(test == 'nan'):
    print('null')
    
    df2.dropna
    print(df2)

