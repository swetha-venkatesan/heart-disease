from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
try:
    with open(r'D:\Appro_Project_1(image_classification)\prediction\copy-heart\model\heart.pickle', 'rb') as file:
        model1 = pickle.load(file)
except Exception as e:
    print(f"Error loading model: {e}")
    model1 = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get form data
        d1 = int(request.form['age'])
        d2 = int(request.form['sex'])        
        d3 = int(request.form['cp'])
        d4 = int(request.form['trestbps'])
        d5 = int(request.form['chol'])
        d6 = int(request.form['fbs'])
        d7 = int(request.form['restecg'])
        d8 = int(request.form['thalach'])
        d9 = int(request.form['exang'])
        d10 = float(request.form['oldpeak'])  # should be float
        d11 = int(request.form['slope'])  
        d12 = int(request.form['ca'])
        d13 = int(request.form['thal'])

        # Create input array for prediction
        arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13]])

        # Predict
        if model1:
            pred1 = model1.predict(arr)
            risk = int(pred1[0])
        else:
            risk = 0  # fallback if model isn't loaded

        # Pass result to template
        return render_template("result.html", risk=risk)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
