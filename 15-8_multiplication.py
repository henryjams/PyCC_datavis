# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:32:08 2022

@author: Hank
"""

from random import randint

from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """Create a class for the die"""
    
    def __init__(self, num_sides = 6):
        """Assume a six-sided die"""
        self.num_sides = num_sides
        
    def roll(self):
        """Return a random value between 1 and num of sides"""
        return randint(1, self.num_sides)
    
# If no argument is passed, die is assumed to be D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_vals = list(range(1, max_result+1))
data = [Bar(x = x_vals, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

plot_title = 'Results of multiplying the rolls of two D6 50,000 times'

my_layout = Layout(title = plot_title, 
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_x_d6.html')