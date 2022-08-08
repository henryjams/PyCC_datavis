# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:34:03 2022

@author: Hank
"""

import csv
import matplotlib.pyplot as plt

from datetime import datetime

sitka_file = 'data/sitka_weather_2018_simple.csv'
death_val_file = 'data/death_valley_2018_simple.csv'

dates, highs, lows = [], [], []

with open(sitka_file) as f:
    reader = csv.reader(f)
    h_r = next(reader)
    
    for row in reader:
        current_date = datetime.strptime(row[h_r.index("DATE")], '%Y-%m-%d')
        try:
            high = int(row[h_r.index("TMAX")])
            low = int(row[h_r.index("TMIN")])
            station_name = str(row[h_r.index('NAME')])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.55)
ax.plot(dates, lows, c='blue', alpha=0.55)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# format plot
chart_title = (f"{station_name} High and Low Temperatures")
chart_title += ('\nDeath Valley, CA and Sitka, AK')
ax.set_title(chart_title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
