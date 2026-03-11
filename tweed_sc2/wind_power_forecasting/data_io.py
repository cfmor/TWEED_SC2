import pandas as pd

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
        df = df.set_index('Time')
        
        # Convert temperature and dew point to °K
        df['temperature_2m'] = (df['temperature_2m'] - 32)*5/9 + 273.15
        df['dewpoint_2m'] = (df['dewpoint_2m'] - 32)*5/9 + 273.15
        
        df_list.append(df)
    
    # Concatenate all dataframes into one
    data = pd.concat(df_list, ignore_index=True)
    
    # Display results
    print(f"Combined DataFrame Shape: {data.shape}")
    print("\nFirst 5 rows:")
    print(data.head())

    return data


