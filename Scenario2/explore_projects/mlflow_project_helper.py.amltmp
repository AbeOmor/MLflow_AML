import mlflow
from azureml.core import Workspace
from urllib.parse import urlparse
import argparse

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--iris-csv", type=str)

    # parse args
    args = parser.parse_args()

    # return args
    return args

if __name__ == "__main__":
    
    experiment_name = 'experiment-with-mlflow-projects'
    mlflow.set_experiment(experiment_name)

    args = parse_args()
    
    backend_config = {"USE_CONDA": False}
    project_uri = "."
    params = {"data_file": args.iris_csv}

    # Run MLflow project and create a reproducible conda environment
    # on a local host
    mlflow.run(project_uri, parameters=params, backend = "azureml", backend_config = backend_config)