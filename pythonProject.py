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

#SET UP DATA FRAMES BY CITY
dsm = df[df.City == 'DES MOINES']
ank = df[df.City == 'ANKENY']
clv = df[df.City == 'CLIVE']
jhn = df[df.City == 'JOHNSTON']
    

#PLOT METHODS

def printAverages(df):
    """prints the averages of data
       Ex. printAverages(ank)"""
    print ('The averages of the data: \n', np.round(df.mean(), decimals=2))

def plotAverageYear(df, year):
    """Given a year, plots the different house prices in that year
       Ex. plotAverageYear(dsm, 1920)"""
    year = int(year)
    titlename = str(year)
    dfYear = df[df.Yr == year]
    dfYear.plot(kind='bar', x='Yr', y='Price', title=' Price of '+ titlename + ' Houses')
    
def plotAverageYearBuilt(df, outliers):
    """Plots the year built and price, with and without outliers
       Ex. plotAverageYearBuilt(clv, False)"""
    if(outliers == True):
        df.plot(kind='scatter', x='Yr', y='Price', title='Year Built vs Price')
    else:
        df3 = df[df.Price < 350000]
        df3.plot(kind='scatter', x='Yr', y='Price', title='Year Built vs Price (No Outliers)')
        
def plotSaleDateAverages(df):
    """Groups Sale Dates together and averages their prices and plots in bar graph
       Ex. plotSaleDateAverages(jhn)"""
    df.groupby('SaleDate').Price.mean().plot(kind='bar', title='Sales Date vs Price')
    
def plotAreaPrice(df):
    """Shows effect on area and price(outliers taken out)
       Ex. plotAreaPrice(df)"""
    df3 = df[df.Price < 350000]
    df3.plot(kind='scatter', x='Area', y='Price', title='Area vs Price (No Outliers)')

def plotBedPrice(df):
    """Groups by number of Total Bedrooms and shows effect on price of house
       Ex. plotBedPrice(ank)"""
    df.groupby('TBr').Price.mean().plot(kind='bar', title='Bedrooms vs Price')

def plotBathPrice(df):
    """Groups by number of Total Bathrooms and shows effect on price of house
       Ex. plotBathPrice(jhn)"""
    df.groupby('Bathrooms').Price.mean().plot(kind='bar', title='Bathrooms vs Price')

def plotBedBath(df):
    """Group by bedrooms and plot bathrooms on y and vice versa
       Ex. plotBedBath(dsm)"""
    df.groupby('TBr').Bathrooms.mean().plot(kind='bar', title='Bedrooms vs Bathrooms')

def plotBathBed(df):
     """Group by bathrooms and plot bedrooms on y
        Ex. plotBathBed(clv)"""
     df.groupby('Bathrooms').TBr.mean().plot(kind='bar', title='Bathrooms vs Bedrooms')
     
def plotCityAverages():
    """Groups by average city price and plots them
        Used only on DataFrame containing all cities
        Ex. plotCityAverages()"""
    df.groupby('City').Price.mean().plot(kind='bar', title='Average price per City')

def plotAverageOnAcre(df):    
    """Plots the average area of house on Acres of land"""
    df.groupby('Acres').Area.mean().plot(kind='bar', title = 'Average area of house on an Acres of land')

def plotAcresWithArea(df):
    """Plot Average acres of land with area of house"""
    df.groupby('Area').Acres.mean().plot(kind='bar', title = 'Average Acres of land with area of house')

def plotAveragePricePerAcre(df):
    """Plots average price per Acre"""
    df.groupby('Acres').Price.mean().plot(kind='bar', title = 'Average Price Per Acre')

def plotAveragePriceOfArea(df):
    """Plots Average price for area of house
       Ex. plotAveragePriceOfArea(ank)"""
    df.groupby('Area').Price.mean().plot(kind='bar', title = 'Average Price for Area of house')


    
def seeFunctions():
     print('Available Functions:')
     print('(1)  plotCityAverages()')
     print('(2)  printAverages()')
     print('(3)  plotAverageYear()')
     print('(4)  plotAverYearBuilt()')
     print('(5)  plotSaleDateAverages()')
     print('(6)  plotAreaPrice()')
     print('(7)  plotBedPrice()')
     print('(8)  plotBathPrice()')
     print('(9)  plotBedBath()')
     print('(10) plotBathBed() \n')
     print('other \n')
     print('(11) plotAverageOnAcre()')
     print('(12) plotAcresWithArea()')
     print('(13) plotAveragePricePerAcre()')
     print('(14) plotAveragePriceOfArea() \n')

     print('Type help(functionName) for description and example.')
     
    
def main():    
    print('\nHello, Welcome to Iowa House Plotter \n')
    print('Available cities: Des Moines (dsm), Ankeny(ank), Clive(clv), & Johnston(jhn) \n')
    print('Enter "seeFunctions()" to see functions in the Console')
    
    
if __name__ == "__main__":
    main()
        




