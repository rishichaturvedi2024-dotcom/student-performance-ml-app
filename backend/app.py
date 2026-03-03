from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
metrics = joblib.load("metrics.pkl")



@app.route("/")
def home():
    return "Student Performance Prediction API is running"



@app.route("/metrics", methods=["GET"])
def get_metrics():
    return jsonify(metrics)



@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_data = pd.DataFrame([data])

 
    for col in input_data.columns:
        if col in encoders:
            input_data[col] = encoders[col].transform(input_data[col])

    prediction = model.predict(input_data)

    return jsonify({
        "predicted_math_score": float(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)