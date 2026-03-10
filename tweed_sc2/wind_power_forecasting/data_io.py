"""
TWEED Special Course 2 - Machine Learning
Wind Forecasting Example

"""

import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC

# 1) Load the data into a pandas DataFrame
data1 = pd.read_csv('./inputs/Location1_train.csv')
data2 = pd.read_csv('./inputs/Location2_train.csv')
data3 = pd.read_csv('./inputs/Location3_train.csv')
data4 = pd.read_csv('./inputs/Location3_train.csv')

Power = data1['Power']

# # or do it this one to combine into one dataframe
# data1 = './inputs/Location1_train.csv'
# data2 = './inputs/Location2_train.csv'
# data3 = './inputs/Location3_train.csv'
# data4 = './inputs/Location3_train.csv'
# file_list = [data1, data2, data3, data4]
# combined_df = pd.concat([pd.read_csv(file) for file in file_list], ignore_index=False)
# print(combined_df)


# 2) Plot timeseries of a selected variable (like wind_speed_100m or Power) f
# or a given site (site 1, 2, 3 or 4) within a specific perid, i.e., a function 
# with variable_name, site_index, starting_time and ending_time as inputs.