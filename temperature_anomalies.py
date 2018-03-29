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

#print('There are', data['TAVG'].isnull().sum(), 'NaN average temperature values.')
#print('There are', data['TMIN'].isnull().sum(), 'NaN minimum temperature values values.')
#print('There are', data['DATE'].count(), 'total days covered by this file.')
#print('The first observation was', data['DATE'].iloc[0])
#print('The last observation was', data['DATE'].iloc[-1])
#print('The average temperature was', data['TAVG'].mean(), 'degrees F.')

### max temperature of summer of 69
summer = data[(data['DATE'] >= 19690510) & (data['DATE'] <= 19690831)]
#print('The max temperature in the summer of 69 was', summer['TMAX'].max(), 'degrees.')

#################
### Problem 2 ###
#################

### create an empty dataframe
monthlyData = pd.DataFrame()

### slice time to monthly values (first convert to str)
data['DATE_str'] = data['DATE'].astype(str)
data['DATE_mo'] = data['DATE_str'].str.slice(start=0, stop=6)

### group data by date
grouped = data.groupby('DATE_mo')

### obtain mean of each month
data.groupby('DATE_mo')['TAVG'].mean()

### add to new dataframe 
monthlyData['TempF'] = data.groupby('DATE_mo')['TAVG'].mean() 

### use function to convert F temps to C

def fahrToCelsius(temp_fahrenheit):
    """ function to convert F temps to C
    Parameters
    ----------
    
    temp_fahrenheit: int | float
        Input temperature in F (number)
    """
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp

### create empty column for function 
colName = 'TempC'
monthlyData[colName]= None

### iterate through F values and update with c
for idx, row in monthlyData.iterrows():
    ### convert F temp to C in each row
    celsius = fahrToCelsius(row['TempF'])
    ### add to new column
    monthlyData.loc[idx, colName] = celsius


### make DATE_mo a column
monthlyData['dateMo'] = monthlyData.index

### reorder
monthlyData = monthlyData[['dateMo', 'TempF', 'TempC']]
monthlyData = monthlyData.reset_index(drop = True)


########################################
############# Problem 3 ################
########################################

### create a new DataFrame
referenceTemps = pd.DataFrame()

### sort data from 1952 to 1980
period = data[(data['DATE'] >= 19520101) & (data['DATE'] <= 19801231)]


### slice by month
period['Month'] = period['DATE_mo'].str.slice(start=4, stop=6)

### group data
grouped2 = period.groupby('Month') 

### obtain mean values
period.groupby('Month')['TAVG'].mean()

### add to new dataframe
referenceTemps['avgTempsC'] = (period.groupby('Month')['TAVG'].mean() -32) / 1.8

### create monthly row index values
rowMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

### add to dataFrame
referenceTemps['Months'] = rowMonth

### reorder dataFrame and drop index
referenceTemps = referenceTemps[['Months', 'avgTempsC']]
referenceTemps = referenceTemps.reset_index(drop = False)

### prepare to join dataframes
### create matching col in monthlyData to match referenceTemps
monthlyData['Month'] = monthlyData['dateMo'].str.slice(start=4, stop=6)

### join
monthlyData = monthlyData.merge(referenceTemps, on='Month')       

### calculate DIFF
monthlyData['DIFF'] = (monthlyData['TempC'] - monthlyData['avgTempsC']) 

### clean dataset    
monthlyData = monthlyData.drop(['TempF', 'Month'], axis=1) 
monthlyData = monthlyData.set_index('dateMo')
monthlyData = monthlyData[['TempC', 'avgTempsC', 'Months', 'DIFF']]

### write to csv  
monthlyData.to_csv('Helsinki_mo.csv', sep=',')
referenceTemps.to_csv('Helsinki_moAgg.csv', sep=',')