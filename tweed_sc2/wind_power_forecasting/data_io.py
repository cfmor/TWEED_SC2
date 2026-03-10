"""
TWEED Special Course 2 - Machine Learning
Wind Forecasting Example

"""

import pandas as pd
import matplotlib.pyplot as plt
import glob

# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC

# 1) Load the data into a pandas DataFrame


# Load into one dataframe retaining the location
files = [
    './inputs/Location1_train.csv', 
    './inputs/Location2_train.csv', 
    './inputs/Location3_train.csv', 
    './inputs/Location4_train.csv'
]

df_list = []
for file in files:
    # Read the CSV
    df = pd.read_csv(file)
    
    # Extract the location name from the filename (e.g., 'Location1')
    loc_name = file.split('/')[2].split('_')[0]
    
    # Add a new column to identify the source location
    df['Location'] = loc_name
    
    # Convert 'Time' to datetime objects for better analysis
    df['Time'] = pd.to_datetime(df['Time'])
    
    df_list.append(df)

# Concatenate all dataframes into one
data = pd.concat(df_list, ignore_index=True)

# Display results
print(f"Combined DataFrame Shape: {data.shape}")
print("\nFirst 5 rows:")
print(data.head())



# 2) Plot timeseries of a selected variable (like wind_speed_100m or Power) f
# or a given site (site 1, 2, 3 or 4) within a specific perid, i.e., a function 
# with variable_name, site_index, starting_time and ending_time as inputs.

# data.plot(x='Time', y='Power')
# plt.show()

locations = data['Location'].unique()
fig, axes = plt.subplots(len(locations), 1, figsize=(12, 4 * len(locations)), sharex=True)

for i, loc in enumerate(locations):
    # Filter data for the specific location
    loc_data = data[data['Location'] == loc]
    
    ax = axes[i]
    ax.plot(loc_data['Time'], loc_data['Power'], color='tab:blue', linewidth=0.5)
    
    # Formatting
    ax.set_title(f'Power Generation over Time: {loc}', fontsize=14)
    ax.set_ylabel('Power Output')
    ax.grid(True, linestyle='--', alpha=0.6)

# Final layout adjustments
axes[-1].set_xlabel('Timestamp')
plt.tight_layout()

# Save and show
plt.savefig('combined_location_plots.png', dpi=300)
print("Process complete. Combined data shape:", data.shape)
plt.show()
