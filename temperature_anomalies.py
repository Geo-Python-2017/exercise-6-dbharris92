# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:48:53 2018
GeoPython Exercise 6 Assignment

Problem 1: Import CSV of precipitation and temperature values from NOAA. Script prints several general values about the data
Problem 2: Calculate monthly average temps

@author: harrisab2
"""
import pandas as pd

### read in CSV, declare NoData (-9999) skiprows must also take list form
data = pd.read_csv('ex6raw.txt', sep= '\s+', skiprows = [1],  dtype = {'PRCP': float, 'TAVG': float, 'TMAX': float, 'TMIN': float}, na_values=[-9999])

### print requested values

print('There are', data['TAVG'].isnull().sum(), 'NaN average temperature values.')
print('There are', data['TMIN'].isnull().sum(), 'NaN minimum temperature values values.')
print('There are', data['DATE'].count(), 'total days covered by this file.')
print('The first observation was', data['DATE'].iloc[0])
print('The last observation was', data['DATE'].iloc[-1])
print('The average temperature was', data['TAVG'].mean(), 'degrees F.')

### max temperature of summer of 69
summer = data[(data['DATE'] >= 19690510) & (data['DATE'] <= 19690831)]
print('The max temperature in the summer of 69 was', summer['TMAX'].max(), 'degrees.')

#################
### Problem 2 ###
#################

### create an empty dataframe
monthyData = pd.DataFrame()

### slice time to monthly values (first convert to str)
data['DATE_str'] = data['DATE'].astype(str)
data['DATE_mo'] = data['DATE_str'].str.slice(start=0, stop=6)




