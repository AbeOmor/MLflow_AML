# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# imports
import os
import mlflow
import sys
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

## User currently needs to add an experiment name. Should not be neccesary in a future relase
mlflow.set_experiment("Scenario2_project")
########

# define functions
def main():
    # enable auto logging
    mlflow.sklearn.autolog(log_input_examples=True)

    # read in alpha
    alpha = str(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    print("alpha value", alpha)
    # process data
    data = process_data()

    # train model
    model = train_model(alpha, data)

    # graoh accuracy
    prediction_compare(model, data)

def process_data():
    # split dataframe into X and y
    X, y = load_diabetes(return_X_y=True)
    columns = ['age', 'gender', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    data = {
         "train": {"X": X_train, "y": y_train},
         "test": {"X": X_test, "y": y_test}}
    
    # return split data
    return data

def train_model(alpha, data):

     mlflow.log_metric("Training samples", len(data['train']['X']))
     mlflow.log_metric("Test samples", len(data['test']['X']))

     # Log the algorithm parameter alpha to the run
     #mlflow.log_metric('alpha', alpha)
     # Create, fit, and test the scikit-learn Ridge regression model
     regression_model = Ridge(alpha=alpha)
     regression_model.fit(data['train']['X'], data['train']['y'])
     
     return regression_model

def prediction_compare(model, data):
    preds = model.predict(data['test']['X'])

    # Log mean squared error
    print('Mean Squared Error is', mean_squared_error(data['test']['y'], preds))
    #mlflow.log_metric('mse', mean_squared_error(data['test']['y'], preds))

    # Save the model to the outputs directory for capture
    #mlflow.sklearn.log_model(model, "model")

    # Plot actuals vs predictions and save the plot within the run
    fig = plt.figure(1)
    idx = np.argsort(data['test']['y'])
    plt.plot(data['test']['y'][idx], preds[idx])
    fig.savefig("actuals_vs_predictions.png")
    mlflow.log_artifact("actuals_vs_predictions.png")

# run script
if __name__ == "__main__":

    # run main function
    main()