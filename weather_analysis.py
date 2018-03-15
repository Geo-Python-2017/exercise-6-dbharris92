# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:29:41 2018

Walk-through of GeoPython Lesson6

@author: Drew
"""
import pandas as pd

### read in csv, sep parameter allows varying number of spaces between columns
### and declare noData values with na_values
data = pd.read_csv('raw.txt', sep='\s+', na_values=['*', '**', '***', '****', '*****', '******'] )

### examine first 5 columns with .head() function
print(data.head())

### check what columns we have
print(data.columns)

### select columns with for unexception weather conditions

select_cols = ['YR--MODAHRMN', 'DIR', 'SPD', 'GUS', 'TEMP', 'MAX', 'MIN']

data = data[select_cols]

### print last 5 rows and datatypes with tail() and dtypes functions

print(data.tail())
print(data.dtypes)

### rename columns with rename()

### first, store new names in a dictonary
name_cd = {'YR--MODAHRMN': 'TIME', 'SPD': 'SPEED', 'GUS':'GUST'} 

### change column names by passing dictionary into parameter columns in rename()
data = data.rename(columns=name_cd)

print(data.columns)

### basic statistics to understand data better with describe()
print(data.describe())

### check first 30 rows with .head()
print(data.head(30))

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

### iterate through data and update new column CELSIUS  with iterrows()

### first create empty column for function

col_name = 'Celsius'
data[col_name] = None


for idx, row in data.iterrows():
    ### convert F temp of row into C
    celsius = fahrToCelsius(row['TEMP'])
    ### add that val to Celsius column
    data.loc[idx, col_name] = celsius

### convert wind speeds into m/s vals

data['SPEED'] = data['SPEED']* 0.44704
data['GUST'] = data['GUST']* 0.44704

### need to compare avg gust and wind speeds, but mismatch of sampling rates (every hr vs 3 times per hour)

### two steps
### convert TIME from int to str
### include only numbers up to hourly accuracy by slicing 

### convert nt to str

data['TIME_str'] = data['TIME'].astype(str)

### slice first ten chars to exclude minute level info
data['TIME_dh'] = data['TIME_str'].str.slice(start=0, stop=10)

### slice only the hour of the day and convert to int
data['TIME_h'] = data['TIME_str'].str.slice(start=8, stop=10)
data['TIME_h'] = data['TIME_h'].astype(int)

### aggregate average temp, wind speed on hourly basis 
###### 1) group the data based on hourly values
###### 2) iterate over those groups and calc avg values of attributes
###### 3) insert those values into a new DataFrame 

### create empty dataframe for aggregated data

aggr_data = pd.DataFrame()

### group data based on TIME_h attribute

grouped = data.groupby('TIME_dh')

### this creates a new object with type dataframegroupby with len of 24

### variable for first hour
time1 = '2017080400'

### get values from DataFrameGroupBy (grouped) with object get_group()
group1 = grouped.get_group(time1)

### use mean() function to calculate mean for DIR, SPEED, GUST, TEMP, Celsius 

### create list with attributes we want
mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP', 'Celsius', 'TIME_h']

### call variable group1 for values for that hour (0400)
mean_values = group1[mean_cols].mean()

### insert datetime valuye from time1 variable 
mean_values['TIME_dh'] = time1

### append to dataFrame with append()



