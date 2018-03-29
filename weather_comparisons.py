# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:43:03 2018
Problem 5 Lesson 6
@author: Drew
"""

import pandas as pd
from datetime import datetime

### read in file
fp = r'F:\GS\harrisab2\S18\GeoViz\Lesson7\sodankyla.txt'
data = pd.read_csv(fp, sep= '\s+', skiprows=[1],na_values=[-9999])

### create avg temp column
data['TAVG'] = (data['TMAX'] + data['TMIN']) / 2

### create a new DataFrame
referenceTemps = pd.DataFrame()

### slice by month
data['DATE_str'] = data['DATE'].astype(str)
data['Month'] = data['DATE_str'].str.slice(start=4, stop=6)

### group data
grouped = data.groupby('Month') 

### obtain mean values
data.groupby('Month')['TAVG'].mean()

### add to new dataframe
referenceTemps['avgTempsC'] = (data.groupby('Month')['TAVG'].mean() -32) / 1.8

### create monthly row index values
rowMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

### add to dataFrame
referenceTemps['Months'] = rowMonth

### reorder dataFrame and drop index
referenceTemps = referenceTemps[['Months', 'avgTempsC']]
referenceTemps = referenceTemps.reset_index(drop = False)

### join
data = data.merge(referenceTemps, on='Month')       

### calculate DIFF
data['DIFF'] = (data['TAVG'] - referenceTemps['avgTempsC']) 

### clean dataset    
#monthlyData = monthlyData.drop(['TempF', 'Month'], axis=1) 
#monthlyData = monthlyData.set_index('dateMo')
#monthlyData = monthlyData[['TempC', 'avgTempsC', 'Months', 'DIFF']]












### calculate monthly temp differences between sodankyla and helsinki

### read in Helsinki data
hm = r'F:\GS\harrisab2\S18\GeoViz\Lesson6\Helsinki_mo.csv'
HelsinkiMo = pd.read_csv(hm, sep= ',')

### create a new dataframe for monthly differences
 