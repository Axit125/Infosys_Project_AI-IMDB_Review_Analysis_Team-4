Step 1: Clone the Repository
Clone the repository to your local machine:
git clone https://github.com/yourusername/IMDB_Review_Analysis.git
cd IMDB_Review_Analysis
Step 2: Install Dependencies
Install all the required Python libraries using:
pip install -r requirements.txt
________________________________________
Step 3: Prepare the Dataset
Download the IMDB Movie Reviews Dataset from Kaggle and save it as IMDB Dataset.csv in the project directory. You can download the dataset from the following link:
IMDB Dataset on Kaggle
Ensure that the dataset is in CSV format and is named correctly.
________________________________________
Step 4: Train the Model
Once the dataset is prepared, run the following script to train the model and save the trained Logistic Regression model along with the TF-IDF Vectorizer:
python train_model.py
This script will generate two files: model_logreg.pkl and vectorizer.pkl, which contain the trained model and the vectorizer, respectively.
________________________________________
Step 5: Run the Streamlit App
Now that the model is trained and saved, you can run the Streamlit app. This will launch the web app where you can enter movie reviews and get predictions.
To start the Streamlit app, run the following command:
streamlit run app.py
________________________________________
Step 6: Using the App
1.	Open the app in your browser (Streamlit will provide a local URL, e.g., http://localhost:8501).
2.	Enter a movie review in the provided input box.
3.	Click Predict to classify the sentiment of the review.
4.	The app will display whether the review is positive or negative.

________________________________________________________________________________

Step-by-Step Instructions for Updating Your GitHub Repository
________________________________________
Step 1: Clone the Repository (if you haven’t done so already)
If you have not cloned the repository to your local machine yet, follow these steps:
1.	Clone the repository: Open a terminal/command prompt and run:
git clone https://github.com/Axit125/Infosys_Project_AI-IMDB_Review_Analysis_Team-4.git
cd Infosys_Project_AI-IMDB_Review_Analysis_Team-4
2.	If you already have the repository cloned, skip this step.
________________________________________
Step 2: Make Changes to Your Code
1.	Open your project folder (Infosys_Project_AI-IMDB_Review_Analysis_Team-4) in your preferred code editor (like VS Code, PyCharm, etc.).
2.	Update your project files:
o	Modify or add new Python code (e.g., app.py, train_model.py, etc.).
o	Update or add any other necessary files like README.md, model files, etc.
3.	After making the necessary changes, save your files.
________________________________________
Step 3: Check the Status of Changes
Before you add your changes to Git, it's a good practice to check the status of your modified files. Open a terminal or command prompt in your project directory and run:
git status
This will display the files that have been modified or added.
________________________________________
Step 4: Add Files to Staging Area
Once you've checked the status, you need to add the files to the staging area so they can be committed. To add all the modified files, run:
git add .
Alternatively, you can specify individual files if you want to add specific ones:
git add app.py README.md train_model.py
________________________________________
Step 5: Commit Your Changes
Now that your files are staged, you can commit your changes to Git with a message. Run the following command:
git commit -m "Updated code for IMDB review analysis, added new features and improved accuracy"
Ensure that your commit message is clear and descriptive of the changes you've made.
________________________________________
Step 6: Push the Changes to GitHub
After committing, you need to push the changes to your GitHub repository. If you are working on the main branch, run:
git push origin main
If you're working on a different branch, replace main with your branch name (e.g., feature-branch).
________________________________________
Step 7: Verify Changes on GitHub
After successfully pushing the changes, go to your GitHub repository at https://github.com/Axit125/Infosys_Project_AI-IMDB_Review_Analysis_Team-4 to verify that the updated files are reflected in the repository. You should see your new commit and updated files.
________________________________________
Summary of Commands
# Clone the repository (if you haven't already)
git clone https://github.com/Axit125/Infosys_Project_AI-IMDB_Review_Analysis_Team-4.git
cd Infosys_Project_AI-IMDB_Review_Analysis_Team-4

# Check the status of changes
git status

# Add all modified files
git add .

# Commit changes with a descriptive message
git commit -m "Updated code for IMDB review analysis, added new features and improved accuracy"

# Push the changes to GitHub
git push origin main

