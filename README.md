# MLFLow integration in AzureML
## E2E Scenarios with DevPlat v2 and MLFlow [4 core scenarios]

### [P0] Scenario 1: Set AML as remote store with MLFlow 
#### Cohort: Getting started with AzureML

1)	User trains locally using MLFlow using MLFlow logging / autologging

2)	Move to AML by setting the tracking URI in the backend (not in my training code), packaging as a project and using the AzureML CLIv2 or MLFlow CLI. The user doesn’t have to change their training or scoring code.

    a.	Users set MLFLOW_TRACKING_URI via CLI

    b.	User should be able to run same code
	
    c.	The user can run that same training script locally and still have everything tracked in AML without updating code

3)	All AML parameters, metrics, models and logged artifacts should show up in AML run history

**NOTE** This only works if the user has set an experiment in their code, if not it break. We need to be able to set a default experiment for the user with now experiment set.

### [P0] Scenario 2: Train and deploy with MLFlow and AML
#### Cohort: ML Builders and ML Pros
1)	Train baseline model and log / autolog with MLFlow and submit job with AML CLI/MLFLow CLI

2)	Test model locally with v2 CLI and manually validate results

3)	Register the model from the run 

4)	{Optional} Change the model stage to “Production” and discuss with team before deploying to production (**NOTE:** Not fully integrate in AML UI yet)
    
5)	After user is satisfied with the model, deploy model on AML to an endpoint and use endpoint to predict all the result from a dataset. (**NOTE: ** TensorSpec not supported yet)

6)	Test your deployed model on sample inputs and validate via AML CLI v2 or MLFLow
- 	a.	[GAP] Get a sample input or signature from MLFLow/AML via CLI or UI. 

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
