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


