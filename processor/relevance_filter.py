
import joblib

vectorizer, model = joblib.load("ml/relevance_model.pkl")

def is_cyber_relevant(text):
    if not text:
        return False
    return len(text) > 10   
