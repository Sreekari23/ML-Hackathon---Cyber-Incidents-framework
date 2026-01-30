
import random
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased"
)


def classify_severity(text):

    t = text.lower()
    if "rce" in t or "remote code execution" in t:
        return "CRITICAL", 0.9
    if "sql injection" in t or "prototype pollution" in t:
        return "HIGH", 0.8
    if "xss" in t or "csrf" in t:
        return "MEDIUM", 0.7
    return "LOW", 0.6
