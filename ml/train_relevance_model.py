import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("ml/train_relevance.csv")

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english", max_features=1500)
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

joblib.dump((vectorizer, model), "ml/relevance_model.pkl")
print("Relevance model trained")
