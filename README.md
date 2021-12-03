# MLFLow integration in AzureML
## E2E Scenarios with DevPlat v2 and MLFlow [4 core scenarios]

### [P0] Scenario 1: Set AML as remote store with MLFlow 
#### Cohort: Getting started with AzureML

1)	User trains locally using MLFlow using MLFlow logging / autologging
2)	Move to AML by setting the tracking URI in the backend (not in my training code). The user doesn’t have to change their training or scoring code.
     
    **a)** [GAP] Help users set MLFLOW_TRACKING_URI via CLI... AzureML is adding MLFLOW_TRACKING_URI to CI by default soon
    
    i.	Use: 
    `export MLFLOW_TRACKING_URI=$(az ml workspace show --query mlflow_tracking_uri | sed 's/"//g')` 
    or 
    `export MLFLOW_TRACKING_URI=$(python -c "from azureml.core import Workspace; print(Workspace.from_config().get_mlflow_tracking_uri())")` 

    **b)** User should be able to run same code 
    
    i.	[GAP] python train.py ... AzureML is adding Default experiment name, perhaps the file name or a GUID) 
    
    ii.	** This only works if the user has set an experiment in their code, if not it break. We need to be able to set a default experiment for the user with now experiment set.

    **c)** The user can run that same training script locally and still have everything tracked in AML without updating code
    
3)	All parameters, metrics, models and logged artifacts should show up in AML run history  

### [P0] Scenario 2: Train and deploy with MLFlow and AML
#### Cohort: ML Builders and ML Pros
1. 1)	Train baseline model and log / autolog with MLFlow and submit job with MLFLow CLI via Projects
- 	a.	Normal Jobs
	- [GAP] `mlflow run https://github.com/mlflow/mlflow-example.git -P alpha=5 --experiment-name="test-abe" --backend azureml `

	- [GAP] `mlflow run sklearn_elasticnet_wine -P alpha=0.42 --backend azureml --experiment-name test-abe2`
- 	b.	AutoML Jobs (Not Supported)
- 	c.	Sweep Job  (Not Supported) 

2)	Test model locally with v2 CLI and manually validate results
- 	a.	Via MLFlow: Retrieve model with MLFLow
- 	b.	[GAP] Via AML CLI: Retrieve model from a run with AML CLI
- - i.	az ml job download -n <job_id>, doesn’t work for local MLFLow Experiements, because these are tracked runs and not jobs. Every Job has a run, not every run is a job.
-  c.	[GAP] Via AML CLI: Local online deployment for manual testing and NCD on v2
- - i.	Not working, need to add support for –local and MLFlow

4)	Register the model from the run 
- 	a.	MLflow allows registering model in 3 different ways. Refer mlflow docs here on how to achieve it. We need to support all 3 well
	- 		i.	mlflow.sklearn.log_model()
	- 		ii.	mlflow.register_model(“runs://”)
	- 		iii.	client.create_registered_model()
- 	b.	[GAP] Via AML CLI: Use v2 CLI to register from a run 
- 	c.	[GAP] Via UI: Right-click the model in a job [Output+Logs] and register as a model

5)	Discuss with other members and stage the model before deployment. Change the model stage to “Production” and discuss with team before deploying to production via AML CLI v2
- 	a.	Via AML CLI, UI or SDK: [GAP] Change stage, via Model stages and discussions or organization-wide feed

----- USER SWITCHES TO CONTROL PLAN ACTIONS ---------

6)	Test your deployed model on sample inputs and validate via AML CLI v2
- 	a.	Download model from registry or retrieve from registry
	- 	i.	[GAP] “az ml model download”
	- 	ii.	Using azureml:model-name in the v2 YAML
- 	b.	Easily Deploy and validate model test inputs via AML UI, CLI or SDK
	- 		i.	AML CLI: az ml online-endpoint invoke --name sklearn-deployment --request-file sample-request-sklearn.json
	- 		ii.	UI: There is a test tab.
	- 		iii.	SDK: ???
	- 		iv.	[GAP] Get a sample input or signature from MLFLow/AML via CLI or UI

7)	After user is satisfied with the model, deploy model on AML to predict all the result from a dataset. 
- 	a.	Via Online or Batch endpoints and NCD 
	- 	i.	Deploy to AML using the AML CLI v2, [GAP] Get the Studio UI link to deployment from CLI output
	- 	ii.	[GAP] Deploy using MLFLow CLI
- 	b.	Deploy to MIR, AML Arc [GAP], and Spark [GAP]

### [P0] Scenario 2b: Collaboration and Compare - AML Run Analysis and Model comparison
#### Cohort: ML Builders and ML Pros 
1.	User A has access to User B’s training metrics and want to compare it their training results. OR User A has done a sweep job and wants to find the best model
2.	Analyze runs (metrics, parameters, etc) interactively 
3.	Use mlflow.search_runs() and other commands to load into Pandas dataframe and do common analysis (mlflow.search_runs())
	a.	compare job A to job B
	b.	find best model in sweep based on primary metric
	c.	find best model in sweep based on some other logged metric etc
  
 ### [P1] Scenario 3: Automation, Pipeline Job and Deploy with MLFlow and AML
 ### [P2] Scenario 4: Retrain Model and Compare Performance and Redeploy with MLFLow 
