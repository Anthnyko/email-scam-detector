import pickle

# Exposes model and vectorizer for uses elsewhere

with open("model/rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
