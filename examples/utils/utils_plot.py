'''
File name: utils_plot.py
    Example code rlated to the tradingti.utils.plot module.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import tradingti.utils.plot as plot
import pandas as pd
from pandas.plotting import register_matplotlib_converters

# Converters used in parsing the dates from csv
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('example_plot.csv', parse_dates = True, index_col = 0)

# Create the plot (with exception handling)
try:
    plt = plot.lineGraph(data = df[['Adj Close']], title = 'Example Graph', 
        x_label = 'Date', y_label = 'Value in $')

except Exception as e:
    print('ERROR:', e)

# Note: Special handling is needed when you call first plt.show() and then
#       the plt.savefig() for the same figure. See: 
#       https://stackoverflow.com/questions/9012487/matplotlib-pyplot-savefig-outputs-blank-image

# Save the created graph
plt.savefig('utils_plot_example.png')

# Show the created graph
plt.show()