import numpy as np

def parse_data(data):
    
    """
    Checks abnormalities in the data frame and replaces them by nan
    """
    
    # 1- Define range for each feature
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

    # 2- Apply masks
    for col, (low, high) in ranges.items():
        if col in data.columns:
            if low is not None:
                data[col].mask(data[col] < low, np.nan, inplace=True)
            if high is not None:
                data[col].mask(data[col] > high, np.nan, inplace=True)
    
    return data