# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:54:42 2022

@author: Hank
"""

import csv
import matplotlib.pyplot as plt

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from datetime import datetime

num_rows = 10_000

filename = 'data/world_fires_7_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lats, lons, brights = [], [], [], []
    hover_text = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        label = f"{date.strftime('%m/%d/%y')} - {brights}"
        bright = float(row[2])
        
        lats.append(row[0])
        lons.append(row[1])
        brights.append(bright)
        hover_text.append(label)
        
        row_num += 1
        if row_num == num_rows:
            break
            
data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker':{
        'size': [bright/20 for bright in brights],
        'color': brights,
        'colorscale': 'YlOrRd', #'Blackbody',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='Global Fire Activity - Last Week', title_x=0.5)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=('16-9_world_fires.html'))