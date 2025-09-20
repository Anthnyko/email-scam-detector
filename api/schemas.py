from pydantic import BaseModel
from typing import List

class EmailRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    flagged_keywords: list[str]   # Shows list of scam phrases in response

class BatchRequest(BaseModel): # Accepts a list of email texts
    texts: list[str]

class BatchResponse(BaseModel):
    results: list[PredictionResponse] # Returns a list of predictions