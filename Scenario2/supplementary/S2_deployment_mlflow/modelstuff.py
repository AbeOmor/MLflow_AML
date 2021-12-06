from random import random, randint
from sklearn.ensemble import RandomForestRegressor

import mlflow
import mlflow.sklearn

## User currently needs to add an experiment name. Should not be neccesary in a future relase
mlflow.set_experiment("model-reg")
########

#Option 1
# with mlflow.start_run(run_name="test123") as run:
#     params = {"n_estimators": 5, "random_state": 42}
#     sk_learn_rfr = RandomForestRegressor(**params)

#     # Log parameters and metrics using the MLflow APIs
#     mlflow.log_params(params)
#     mlflow.log_param("param_1", randint(0, 100))
#     mlflow.log_metrics({"metric_1": random(), "metric_2": random() + 1})

#     # Log the sklearn model and register as version 1
#     mlflow.sklearn.log_model(
#         sk_model=sk_learn_rfr,
#         artifact_path="sklearn-model",
#         registered_model_name="sk-learn-random-forest-reg-model"
#     )

#Option 2
# from mlflow.tracking import MlflowClient

# client = MlflowClient()
# client.create_registered_model("sk-learn-random-forest-reg-model12")

#Option 3
result = mlflow.register_model(
    "runs:/d6f28473-4ad4-48cb-a47d-019d72d90ea9/sklearn-model",
    "sk-learn-random-forest-reg12"
)