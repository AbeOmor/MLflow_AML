# imports
import os
import mlflow
import sys

import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# define functions
def main():
    # enable auto logging
    mlflow.autolog()

    # read in data
    data_file = str(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    df = pd.read_csv(data_file)

    # process data
    X_train, X_test, y_train, y_test = process_data(df)

    # train model
    model = train_model( X_train, X_test, y_train, y_test)


def process_data(df):
    # split dataframe into X and y
    X = df.drop(["species"], axis=1)
    y = df["species"]

    # train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # return split data
    return X_train, X_test, y_train, y_test


def train_model(X_train, X_test, y_train, y_test):
    # train model
    model = SVC()
    model = model.fit(X_train, y_train)

    # return model
    return model


# run script
if __name__ == "__main__":

    # run main function
    main()

