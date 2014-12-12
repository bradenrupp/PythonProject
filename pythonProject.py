# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 20:33:58 2014

@author: mshep
"""

import pandas as pd
import numpy as np


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

def plotCityBedAverages():
    """Grups by average city bedrooms and plots them 
       Used only on DataFrame containing all cities
       Ex. plotCityBedAverages()"""
    df.groupby('City').TBr.mean().plot(kind='bar', title='Average bedrooms per City')

def plotCityBathAverages():
    """Groups by average city bathrooms and plots
       Used only on DataFrame containing all cities
       Ex. plotCityBathAverages()""" 
    df.groupby('City').Bathrooms.mean().plot(kind='bar', title='Average bathrooms per City')

def plotCitySqFtAverages():
    """Groups by average city house square footage and plots
       Used only on DataFrame containing all cities
       Ex. plotCitySqFtAverages()"""
    df.groupby('City').Area.mean().plot(kind='bar', title='Average Sq Ft per City')

def plotCityLotSizeAverages():
    """Groups by city and shows the average house acreage and pots
       Used only on DataFrame containing all cities
       Ex. PlotCityLotSizeAverages"""
    df.groupby('City').Acres.mean().plot(kind='bar', title='Average Acres per City')

    
def seeFunctions():
     print('Available Functions: \n')
     print('(1)  printAverages()')
     print('(2)  plotAverageYear()')
     print('(3)  plotAverYearBuilt()')
     print('(4)  plotSaleDateAverages()')
     print('(5)  plotAreaPrice()')
     print('(6)  plotBedPrice()')
     print('(7)  plotBathPrice()')
     print('(8)  plotBedBath()')
     print('(9) plotBathBed() \n')
     print('other \n')
     print('(10) plotAverageOnAcre()')
     print('(11) plotAcresWithArea()')
     print('(12) plotAveragePricePerAcre()')
     print('(13) plotAveragePriceOfArea() \n')
     print('All City \n')
     print('(14) plotCityAverages()')
     print('(15) plotCityBedAverages()')
     print('(16) plotCityBathAverages()')
     print('(17) plotCitySqFtAverages()')
     print('(18) plotCityLotSizeAverages() \n')

     print('Type help(functionName) for description and example.')
     
    
def main():    
    print('\nHello, Welcome to Iowa House Plotter \n')
    print('Available cities: Des Moines (dsm), Ankeny(ank), Clive(clv), & Johnston(jhn) \n')
    print('Enter "seeFunctions()" to see functions in the Console')
    
    
if __name__ == "__main__":
    main()
    
#PRESENTATION
#df.head()
#df.City.unique()
#df.City.count()

