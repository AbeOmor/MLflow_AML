#!/bin/bash

##Get Tracking URI
export MLFLOW_TRACKING_URI=$(az ml workspace show --query mlflow_tracking_uri -o tsv)

## Print tracking URI
echo $MLFLOW_TRACKING_URI

##Submit Project
mlflow run simple_project -P alpha=0.42 --experiment-name="Scenario2_project" --backend azureml --backend-config=backend_config_local.json

##Retrieve model from Run and Test Model
#Not support in MLFlow CLI

##Register Model
#Not support in MLFlow CLI

##Transistion Model Stage
#Not support in MLFlow CLI

##Deploy Model
mlflow deployments create --name mlflowscenario2 --model-uri models:/scenario2model/1 --target $MLFLOW_TRACKING_URI --config deploy-config-file=deployment_config_v2.json