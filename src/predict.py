from src.model_loader import model, vectorizer

def classify_email(text: str):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    confidence = model.predict_proba(vec)[0][1]     # Confidence score
    label = "Scam" if prediction == 1 else "Safe"
    return label, round(confidence, 2)     # Returns label and confidence score
