# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load the IMDB dataset (make sure the dataset is in the same folder or adjust the path)
data = pd.read_csv('IMDB Dataset.csv')  # Make sure the path is correct to your dataset

# Preview the first few rows of the dataset
print(data.head())

# Assign features and labels
X = data['review']
y = data['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

# Save the trained model and the vectorizer to disk
with open("model_logreg.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

# Print success message
print("Model and vectorizer have been saved successfully!")
