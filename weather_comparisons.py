# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:43:03 2018
Problem 5 Lesson 6
@author: Drew
"""

import pandas as pd
from datetime import datetime

### read in file
fp = 'sodankyla.txt'
data = pd.read_csv(fp, sep= '\s+', skiprows=[1],na_values=[-9999])

### create copy for future
reference = data.copy()

### convert Date column to datetime and make index
data['DATE'] = pd.to_datetime(data['DATE'].astype(str), format='%Y%m%d')
data = data.set_index('DATE')

### create temperature average columb
data['TAVG'] = (data['TMAX'] + data['TMIN']) / 2

### monthly reaggregate 
monthly = data.resample('M').mean()

### wrong method


