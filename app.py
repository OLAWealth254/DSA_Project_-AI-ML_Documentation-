
from flask import Flask, render_template, request
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        input_features = [float(x) for x in request.form.values()]
        prediction = model.predict([input_features])[0]
        result = "High Risk" if prediction == 1 else "Low Risk"
        return render_template("index.html", prediction_text=f"Diabetes Risk Prediction: {result}")
    except:
        return render_template("index.html", prediction_text="Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)
