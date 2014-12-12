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
from datetime import datetime


filename = "results2.csv"

#Reads csv file into dataframe
df = pd.read_csv(filename, encoding='latin1')

#Strips off information we don't need about the date
df['SaleDate'] = df['SaleDate'].map(lambda x: str(x)[6:])
#Converts date to int
df['SaleDate'] = df['SaleDate'].astype(int)

#Drops any rows that do not contain any information in them
df = df.dropna(how='any')

#Sale date
format = "%Y"
times = pd.to_datetime(df.SaleDate, format=format)
df.set_index(times, inplace=True)



#Which has more effect bathroom or bedrooms on price
#This is how you choose columns:
#df.ix[:,['TBr', 'Bathrooms', 'Price']]
#not sure what to do with the graph 


#PLOT METHODS

def printAverages():
    print ('The averages of the data: \n', np.round(df.mean(), decimals=2))

def plotAverageYear(year):
    """Given a year, plots the different house prices in that year"""
    year = int(year)
    titlename = str(year)
    dfYear = df[df.Yr == year]
    dfYear.plot(kind='bar', x='Yr', y='Price', title='Average Price of '+ titlename + ' Houses')
    
def plotAverageYearBuilt(outliers):
    """Plots the year built and price, with and without outliers"""
    if(outliers == True):
        df.plot(kind='scatter', x='Yr', y='Price', title='Year Built vs Price')
    else:
        df3 = df[df.Price < 350000]
        df3.plot(kind='scatter', x='Yr', y='Price', title='Year Built vs Price (No Outliers)')
        
def plotSaleDateAverages():
    """Groups Sale Dates together and averages their prices and plots in bar graph"""
    df.groupby('SaleDate').Price.mean().plot(kind='bar', title='Sales Date vs Price')
    
def plotAreaPrice():
    """Shows effect on area and price(outliers taken out)"""
    df3 = df[df.Price < 350000]
    df3.plot(kind='scatter', x='Area', y='Price', title='Area vs Price (No Outliers)')

def plotBedPrice():
    """Groups by number of Total Bedrooms and shows effect on price of house"""
    df.groupby('TBr').Price.mean().plot(kind='bar', title='Bedrooms vs Price')

def plotBathPrice():
    """Groups by number of Total Bathrooms and shows effect on price of house"""
    df.groupby('Bathrooms').Price.mean().plot(kind='bar', title='Bathrooms vs Price')

def plotBedBath():
    """Group by bedrooms and plot bathrooms on y and vice versa"""
    df.groupby('TBr').Bathrooms.mean().plot(kind='bar', title='Bedrooms vs Bathrooms')

def plotBathBed():
     """Group by bathrooms and plot bedrooms on y"""
     df.groupby('Bathrooms').TBr.mean().plot(kind='bar', title='Bathrooms vs Bedrooms')

        
    
        
        




