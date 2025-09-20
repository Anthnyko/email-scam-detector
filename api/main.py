from fastapi import FastAPI
from api.schemas import EmailRequest, PredictionResponse, BatchRequest, BatchResponse
from src.predict import classify_email
from src.flagger import flag_keywords
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
    keywords = flag_keywords(request.text)   # Check input email for scam phrases
    logger.info(f"Prediction: {label}, Confidence: {confidence}, Keywords: {keywords}")
    return PredictionResponse(prediction=label, confidence=confidence, flagged_keywords=keywords)  # Returns structured response

@app.post("/batch_predict", response_model=BatchResponse)
def batch_predict(request: BatchRequest):
    results = []
    for text in request.texts:       # Loops through each email requested
        label, confidence = classify_email(text)
        keywords = flag_keywords(text) 
        results.append(PredictionResponse(prediction=label, confidence=confidence, flagged_keywords=keywords))   # Adds prediction and scoring into list
    return BatchResponse(results=results)   # Returns a structured list of results