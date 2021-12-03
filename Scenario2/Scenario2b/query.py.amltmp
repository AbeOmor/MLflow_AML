from mlflow.tracking.client import MlflowClient
from mlflow.entities import ViewType

run = MlflowClient().search_runs(
  experiment_ids="0",
  filter_string="",
  run_view_type=ViewType.ACTIVE_ONLY,
  max_results=1,
  order_by=["metrics.accuracy DESC"]
)[0]