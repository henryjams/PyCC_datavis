# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 12:35:40 2022

@author: hspra
"""

import csv
import matplotlib as plt

from statistics import mean
from datetime import datetime

# File handling
filename = 'data/new_orleans_2022_daily_weather.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Assemble a list of all dates in the file
    dates = []
    for row in reader:
        try:
            date = (row[2])
        except ValueError:
            continue
        else:
            if date not in dates:
                dates.append(date)
            else:
                break
    
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs_for_date = []
    for date in dates:
        for row in reader:
            if row[2] == date:
                try:
                    TMAX = int(row[6])
                except ValueError:
                    continue
                else:
                    highs_for_date.append(TMAX)
            else:
                continue
    high_avgs = mean(highs_for_date)
                        
print(highs_for_date)            
print(high_avgs)