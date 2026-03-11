"""
Load and parse data 
"""
import numpy as np
from data_io import load_data

files = [
    './inputs/Location1_train.csv', 
    './inputs/Location2_train.csv', 
    './inputs/Location3_train.csv', 
    './inputs/Location4_train.csv'
]

data = load_data(files)
    
# check for abnormal values

ranges = {
'temperature_2m': (-100, 100),
'dewpoint_2m': (-100, 100),
'relativehumidity_2m': (0, 100),
'windspeed_10m': (0, None),
'windspeed_100m': (0, None),
'winddirection_10m': (0, 360),
'winddirection_100m': (0, 360),
'Power': (0, None)
}

# 2. Iterate and apply masks
for col, (low, high) in ranges.items():
    if col in data.columns:
        if low is not None:
            data[col].mask(data[col] < low, np.nan, inplace=True)
        if high is not None:
            data[col].mask(data[col] > high, np.nan, inplace=True)

        
        

