"""
TWEED Special Course 2 - Machine Learning
Wind Forecasting Example

Carlos, Kenza, Bassey and Kelley
"""

# 1) Load the data into a pandas DataFrame retaining the location
files = [
    './inputs/Location1_train.csv', 
    './inputs/Location2_train.csv', 
    './inputs/Location3_train.csv', 
    './inputs/Location4_train.csv'
]

from data_io import load_data
data = load_data(files)

# 2) Plot timeseries of a selected variable (like wind_speed_100m or Power) 
# for a given site (site 1, 2, 3 or 4) within a specific perid, i.e., a function 
# with variable_name, site_index, starting_time and ending_time as inputs.

from plot_data import plot_location_data
plot_location_data(data,'Power','Location1')
plot_location_data(data,'windspeed_100m','Location1')


from plot_data import plot_all_location_data
plot_all_location_data(data,'Power')
plot_all_location_data(data,'windspeed_10m')
plot_all_location_data(data,'windspeed_100m')
plot_all_location_data(data,'windgusts_10m')
plot_all_location_data(data,'wdcos_10')
plot_all_location_data(data,'wdcos_100')
plot_all_location_data(data,'temperature_2m')
plot_all_location_data(data,'dewpoint_2m')
plot_all_location_data(data,'relativehumidity_2m')

#3) Compute mean squared error (MSE), mean absolute error (MAE), and root mean 
# square error (RMSE) for a forecasted time series against the corresponding real time series.


# 4) Split the dataset into training dataset and test dataset.