# app.py

import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to load the model and vectorizer
@st.cache_data
def load_model():
    # Load the pre-trained model and vectorizer
    with open("model_logreg.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Load the model and vectorizer into memory
model, vectorizer = load_model()

# Streamlit app layout
st.title("IMDB Movie Review Sentiment Analysis")
review = st.text_area("Enter your movie review:")

if st.button("Predict"):
    # Vectorize the input review
    review_vectorized = vectorizer.transform([review])

    # Predict sentiment (0 = Negative, 1 = Positive)
    prediction = model.predict(review_vectorized)[0]

    # Display result
    if prediction == 1:
        st.success("This is a positive review!")
    else:
        st.error("This is a negative review!")
