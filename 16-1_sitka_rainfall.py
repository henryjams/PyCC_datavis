# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 12:35:40 2022

@author: hspra
"""

import csv
import matplotlib.pyplot as plt

from datetime import datetime

# File
filename = 'data/sitka_weather_2018_simple.csv'

# Open the file and read dates and precip data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            PRCP = float(row[3])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            precips.append(PRCP)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue', alpha=.75)

# Format plot
ax.set_title('Daily Precipitation - 2018\nSitka, AK', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation (in)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()