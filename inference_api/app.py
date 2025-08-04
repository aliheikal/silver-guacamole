from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import logging
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("inference_api/model.pkl")

logging.basicConfig(filename="inference_api/inference.log", level=logging.INFO)

class Input(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Input):
    features = np.array(data.features)
    prediction = model.predict([features])[0]
    timestamp = datetime.utcnow().isoformat()
    mean = np.mean(features)
    std = np.std(features)
    minimum = np.min(features)
    maximum = np.max(features)
    log_entry = (
        f"{timestamp} | INPUT: {data.features} | PREDICTION: {prediction} "
        f"| MEAN: {mean:.2f} | STD: {std:.2f} | MIN: {minimum:.2f} | MAX: {maximum:.2f}"
    )
    logging.info(log_entry)
    return {"prediction": int(prediction)}
