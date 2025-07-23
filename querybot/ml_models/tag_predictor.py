# ml_models/tag_predictor.py
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample data (replace with your question data later)
questions = [
    "How do I debug a Python script?",
    "What is the difference between list and tuple in Python?",
    "How to calculate the derivative of x^2?",
]
tags = [
    "python,debugging",
    "python,data-structures",
    "math,calculus",
]

# Create ml_models directory if it doesn't exist
os.makedirs('ml_models', exist_ok=True)

# Create a pipeline with TF-IDF vectorizer and Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(questions, tags)

# Function to predict tags for a new question
def predict_tags(question_text):
    predicted_tags = model.predict([question_text])
    return predicted_tags[0]

# Example usage
new_question = "How to optimize a Django query?"
predicted_tags = predict_tags(new_question)
print(f"Predicted tags for '{new_question}': {predicted_tags}")

# Save the model
joblib.dump(model, 'ml_models/tag_model.pkl')
print("Model saved successfully!")