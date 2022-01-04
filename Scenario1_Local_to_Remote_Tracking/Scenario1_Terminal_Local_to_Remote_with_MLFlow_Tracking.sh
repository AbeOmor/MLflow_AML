#!/bin/bash

## Train on CI without MLFlow Tracking
python train.py

## Get and store tracking URI
export MLFLOW_TRACKING_URI=$(az ml workspace show --query mlflow_tracking_uri -o tsv)

## Print tracking URI
echo $MLFLOW_TRACKING_URI

## Train on CI with MLFlow Tracking
python train.py