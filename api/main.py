from fastapi import FastAPI
from pydantic import BaseModel
import mlflow

mlflow.set_tracking_uri("sqlite:////app/db/mlflow.db")

app = FastAPI()

class ExperimentData(BaseModel):
    experiment_name: str
    param: str
    value: str

@app.post("/track-experiment")
async def track_experiment(data: ExperimentData):    
    
    mlflow.set_experiment(data.experiment_name)

    with mlflow.start_run():
        mlflow.log_param(data.param, data.value)
        
    return {"message": "Experiment tracked successfully!"}

    
