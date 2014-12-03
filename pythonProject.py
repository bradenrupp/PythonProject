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

filename = "results.csv"

df = pd.read_csv(filename, encoding='latin1')

#print(df.iloc[1])

#print(df.iloc[44])

#print(df.iloc[44][3])

test = str(df.iloc[44][0])

if(test == 'nan'):
    print('null')


for x in df:
    print(df.iloc[x])
    
    
"""y = 0
    while(y<8):
        if(df[x][y] == null):"""
            
        
    