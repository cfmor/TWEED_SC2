import pandas as pd
import numpy as np

def load_data(files):
    """
    Loads data from csv files and saves to a dataframe
    """
    df_list = []
    for file in files:
        # Read the CSV
        df = pd.read_csv(file)
        
        # Extract the location name from the filename (e.g., 'Location1')
        loc_name = file.split('/')[2].split('_')[0]
        
        # Add a new column to identify the source location
        df['Location'] = loc_name
        
        # Convert 'Time' to datetime objects for better analysis
        df['Time'] = pd.to_datetime(df['Time'],  format="%Y-%m-%d %H:%M:%S")
        # df = df.set_index('Time').sort_index()
        
        # Convert temperature and dew point to °K
        df['temperature_2m'] = (df['temperature_2m'] - 32)*5/9 + 273.15
        df['dewpoint_2m'] = (df['dewpoint_2m'] - 32)*5/9 + 273.15
        
        # Transform the wind direction
        df['wdcos_10'] = np.cos(np.radians(df['winddirection_10m']))
        df['wdsin_10'] = np.sin(np.radians(df['winddirection_10m']))

        df['wdcos_100'] = np.cos(np.radians(df['winddirection_100m']))
        df['wdsin_100'] = np.sin(np.radians(df['winddirection_100m']))

        # df.drop(['winddirection_10m', 'winddirection_100m'], axis=1, inplace=True)

        df_list.append(df)
    
    # Concatenate all dataframes into one
    data = pd.concat(df_list, ignore_index=True)
    
    # Display results
    print(f"Combined DataFrame Shape: {data.shape}")
    print("\nFirst 5 rows:")
    print(data.head())

    return data


