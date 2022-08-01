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

daily_high_avg = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        current_date = row[2]
        for row in reader:
            if current_date == row[2]:
                try:
                    high = int(row[6])
                except ValueError:
                    continue
                else:
                    highs.append(high)
                    
daily_high_avg.append(mean(highs))
            
print(highs)
print(daily_high_avg)