# coding: utf-8
import sys
import pandas as pd
import numpy as np
from sklearn import metrics

# load scored data
scored_path = sys.stdin
scored_df = pd.read_csv(scored_path, sep = ',')

# evaluation stats function
def evaluate(scored_df):
    # get real age
    Y = scored_df['Age'].values
    # get predicted age
    pred = scored_df['Predicted Age'].values
    # calculate r^2 score
    r2 = metrics.r2_score(Y, pred)
    # calculate mean absolute error
    mae = metrics.mean_absolute_error(Y, pred)
    # calculate mean squared error
    mse = metrics.mean_squared_error(Y, pred)
    # calculate root mean squared error
    rmse = np.sqrt(mse)
    # write stats to dictionary
    stats = {'r2_score': r2, 'mean_absolute_error': mae,
             'mean_squared_error': mse, 'root_mean_squared_error': rmse}
    return stats

# evaluate prediction
stats = evaluate(scored_df)

# print result
print(stats)