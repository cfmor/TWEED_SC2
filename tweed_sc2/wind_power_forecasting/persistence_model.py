import pandas as pd

def pm_model(df, location, time): 

    """
    Defining persistence ML model
    df: is the data frame containing all data from all locations
    time: the future date time (YMD H)

    """
    location = "Location" + str(location)

    time = pd.to_datetime(time,  format="%Y%m%d %H") - pd.Timedelta(hours = 1)

    df = df.loc[(time, location)]
    power = df.Power

    return power




