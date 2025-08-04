from zenml import pipeline
from zenml_pipeline.steps.train_step import train_model

@pipeline
def training_pipeline():
    train_model()
