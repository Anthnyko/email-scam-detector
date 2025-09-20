from pydantic import BaseModel
from typing import List

class EmailRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float

class BatchRequest(BaseModel): # Accepts a list of email texts
    texts: List[str]

class BatchResponse(BaseModel):
    results: List[PredictionResponse] # Returns a list of predictions