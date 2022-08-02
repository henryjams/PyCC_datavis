# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:50:04 2022

@author: hspra
"""

import csv
import matplotlib.pyplot as plt

from datetime import datetime

sitka_file = 'data/sitka_weather_2018_simple.csv'
death_val_file = 'data/death_valley_2018_simple.csv'

def get_weather_data(filename, dates, highs, lows, date_index, high_index, 
                     low_index):
    """Reads csv and returns date, high, low values"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
# get sitka data from file
dates, highs, lows = [], [], []
get_weather_data(sitka_file, dates, highs, lows, 2, 5, 6)

# plot stika
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.55)
ax.plot(dates, lows, c='blue', alpha=0.55)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# get death valley data from file
dates, highs, lows = [], [], []
get_weather_data(death_val_file, dates, highs, lows, 2, 4, 5)

# plot death valley
ax.plot(dates, highs, c='red', alpha=0.25)
ax.plot(dates, lows, c='blue', alpha=0.25)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# format plot
chart_title = ('2018 High and Low Daily Temperature Comparison')
chart_title += ('\nDeath Valley, CA and Sitka, AK')
ax.set_title(chart_title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()





