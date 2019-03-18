# coding: utf-8
import sys
import pickle
import pandas as pd
import numpy as np

# load regression model pkl
model_path = sys.argv[1]
model = pickle.load(open(model_path, 'rb'))

# load input data
input_path = sys.stdin
input_df = pd.read_csv(input_path, sep = ',', header = None)
# check if there are column names in the first row
if input_df[0][0] == 'Sex':
    input_df = input_df.drop(input_df.index[0], axis = 0).reset_index(drop = True)
# define columns
column_name = ['Sex', 'Length', 'Diameter', 'Height', 'Weight', 'Shucked Weight',
               'Viscera Weight', 'Shell Weight', 'Age']
input_df.columns = column_name

# data cleansing and feature engineering
def data_processing(input_df):
    # dummy for sex
    sex_dum = pd.get_dummies(input_df['Sex'], prefix = 'Sex')
    df = pd.concat([input_df , sex_dum], axis = 1)
    # convert variable type
    float_cols = ['Length', 'Diameter', 'Height', 'Weight', 'Shucked Weight',
                  'Viscera Weight', 'Shell Weight']
    for i in float_cols:
        df[i] = df[i].astype(float)
    # convert age as int
    df['Age'] = df['Age'].astype(int)
    # generate weight error variable
    total_weight = df['Shell Weight'] + df['Shucked Weight'] + df['Viscera Weight']
    df['Weight Error'] = df['Weight'] - total_weight
    # generate interaction features
    # define feature groups
    binary_cols = ['Sex_F', 'Sex_I', 'Sex_M']
    continuous_cols = ['Length', 'Diameter', 'Height', 'Weight', 'Shucked Weight',
                       'Viscera Weight', 'Shell Weight']
    # interaction features between binary and continuous variables
    for i in binary_cols:
        x1 = df[i]
        for j in continuous_cols:
            x2 = df[j]
            df[i + '_x_' + j] = x1*x2
    # interaction features among continuous variables
    for i in continuous_cols:
        x1 = df[i]
        for j in continuous_cols:
            if i != j:
                x2 = df[j]
                df[i + '_x_' + j] = x1*x2
    # fill missing
    clean_df = df.fillna(0)
    # delete original sex and age
    del clean_df['Sex']
    del clean_df['Age']
    return clean_df

# ensemble scoring by 4 regression models 
def scoring(input_df, clean_df, model):
    # load single regression model
    BR = model['BR']
    Ridge = model['Ridge']
    Lasso = model['Lasso']
    XGB = model['XGB']
    # predict
    BR_test_pred = BR.predict(clean_df.values)
    Ridge_test_pred = Ridge.predict(clean_df.values)
    Lasso_test_pred = Lasso.predict(clean_df.values)
    XGB_test_pred = XGB.predict(clean_df.values)
    # ensemble prediction
    pred = np.round((BR_test_pred + Lasso_test_pred + XGB_test_pred + Ridge_test_pred) / 4)
    # define output columns
    scored_df = input_df.copy()
    # add predicted age
    scored_df['Predicted Age'] = pred.astype(int)
    return scored_df

# execute clean processing on input data
clean_df = data_processing(input_df)
# execute scoring and return scored data
scored_df = scoring(input_df, clean_df, model)

# save result
scored_df.to_csv(sys.stdout, sep = ',', index = False)