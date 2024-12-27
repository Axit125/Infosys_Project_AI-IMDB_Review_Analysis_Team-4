# IMDB Review Analysis - AI Project

## Overview
This project performs sentiment analysis on IMDB movie reviews using machine learning. The model is trained using a variety of preprocessing techniques and a classification algorithm to predict whether a review is positive or negative.

## Features
- Sentiment analysis of IMDB reviews (Positive/Negative).
- Uses `Logistic Regression` for classification.
- Preprocessing techniques include TF-IDF Vectorization and stop words removal.
- Deployed using Streamlit for interactive web app experience.

## Technologies Used
- Python
- Scikit-learn
- Streamlit
- Pickle (for model serialization)

## Files
- **app.py**: Main application file for Streamlit deployment.
- **train_model.py**: Contains the training logic and saves the model.
- **model_logreg.pkl**: Trained logistic regression model.
- **vectorizer.pkl**: TF-IDF vectorizer for text transformation.
- **README.md**: Project documentation.

## How to Run

## 1. Clone the repository:

   git clone https://github.com/Axit125/Infosys_Project_AI-IMDB_Review_Analysis_Team-4.git
   
   cd Infosys_Project_AI-IMDB_Review_Analysis_Team-4
   
## 2. Install dependencies:

pip install -r requirements.txt

## 3. Run the Streamlit app:

streamlit run app.py

Open your browser to view the app.

## Requirements

Python 3.x

streamlit

scikit-learn

pandas

numpy

## Contributing
Feel free to fork this project and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

This completes the instructions on how to run the project and includes the additional step for retraining the model and updating the necessary files.
