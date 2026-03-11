
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

def metrics(predicted, targets):
    """
    Compute the metrics for wind power forecasting.

    Args:
        predicted (np.ndarray): The predicted values.
        targets (np.ndarray): The true values.
    Returns:
        tuple: A tuple containing the computed metrics (MAE, MSE, RMSE).
    """
    
    mae = mean_absolute_error(targets, predicted)
    mse = mean_squared_error(targets, predicted)
    rmse = root_mean_squared_error(targets, predicted)
    return (mae, mse, rmse)


#%% 
# import numpy as np

# target = np.random.rand(100)
# predicted = np.random.rand(100)

# results = metrics(predicted, target)
# print(results)

