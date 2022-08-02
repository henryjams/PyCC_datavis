# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 12:35:40 2022

@author: hspra
"""

import csv
import matplotlib as plt

from datetime import datetime

# File handling
filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    print(header_row)
