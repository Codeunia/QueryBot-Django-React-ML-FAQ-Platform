import joblib
from django.http import HttpResponse

# Load the pre-trained model
model = joblib.load('ml_models/tag_model.pkl')

def home(request):
    # Example new question
    new_question = "How to optimize a Django query?"
    # Predict tags
    predicted_tags = model.predict([new_question])[0]
    return HttpResponse(f"Welcome to QueryBot! Predicted tags: {predicted_tags}")

