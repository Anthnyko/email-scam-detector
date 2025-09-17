from fastapi import FastAPI
from api.schemas import EmailRequest, PredictionResponse
from src.predict import classify_email

app = FastAPI(title="Email Scam Detector")    # Creates API app

@app.get("/")    # Root endpoint for health checks
def read_root():
    return {"message": "Scam Detector API is live!"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: EmailRequest):                    # Accepts email texts
    label, confidence = classify_email(request.text)   # Runs prediction with function
    return PredictionResponse(prediction=label, confidence=confidence)  # Returns structured response