from fastapi import FastAPI
from api.schemas import EmailRequest, PredictionResponse
from src.predict import classify_email
import logging
logging.basicConfig(
    level=logging.INFO,               # Set log level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)
logger = logging.getLogger(__name__)  # Create a logger for this module

app = FastAPI(title="Email Scam Detector")    # Creates API app

@app.get("/")
def read_root():
    return {
        "project": "Email Scam Detector",
        "author": "Anthony Co",
        "version": "1.0",
        "docs": "/docs"
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(request: EmailRequest):                    # Accepts email texts
    logger.info(f"Received email text: {request.text}")
    label, confidence = classify_email(request.text)   # Runs prediction with function
    logger.info(f"Prediction: {label}, Confidence: {confidence}")
    return PredictionResponse(prediction=label, confidence=confidence)  # Returns structured response