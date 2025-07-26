# heart-disease

Heart Disease Prediction
A beginner-friendly, Flask-based web app utilizing a machine learning model (scikit-learn) to predict the likelihood of heart disease using medical input features. The app provides fast, interactive risk estimation to support early decision making.

🚀 Project Overview
This project helps users estimate their risk of heart disease by entering health information such as age, blood pressure, cholesterol, and heart rate. It leverages a trained ML model for efficient, real-time predictions served via a simple and user-friendly web interface.

✨ Features
Input form for key risk factors (age, BP, cholesterol, heart rate, etc.)

Real-time risk prediction (heart disease likelihood)

Interpretable model outputs

Lightweight, responsive HTML frontend

Easy local setup and modular code structure

🛠 Tech Stack
Layer	Tools & Frameworks
Backend	Flask, Python
ML/Modeling	scikit-learn, pickle
Frontend	HTML, CSS
Data Source	Kaggle (Heart Disease dataset)
📦 Folder Structure
text
heart-disease-prediction/
│
├── static/                # CSS, images, etc.
├── templates/             # HTML templates
├── model/                 # Trained pickle model
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── README.md
└── LICENSE
📑 Dataset Description
Source: Kaggle Heart Disease Dataset

Features Used:

Age

Sex

Blood Pressure (RestingBP)

Cholesterol

Maximum Heart Rate

Other clinical indicators

Target: Presence of heart disease (binary classification)

📈 Model Output
Output: Probability (0-1 or %) indicating the risk of heart disease

Algorithm: (e.g., Logistic Regression, Random Forest) trained with scikit-learn

Serialization: Model saved via Python pickle for use in the Flask app

⚙️ Installation Guide
Clone the repository:

bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
Create a virtual environment (optional but recommended):

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the requirements:

bash
pip install -r requirements.txt
▶️ How to Run Locally
Ensure you are in the project directory and activate your environment (if using).

Run the Flask server:

bash
python app.py
Open your browser to: http://localhost:5000

