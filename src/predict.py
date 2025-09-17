from model_loader import model, vectorizer

def classify_email(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return "Scam" if prediction == 1 else "Safe"
