import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    gender: "",
    "race/ethnicity": "",
    "parental level of education": "",
    lunch: "",
    "test preparation course": "",
    "reading score": "",
    "writing score": ""
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", form);
      setPrediction(res.data.predicted_math_score.toFixed(2));
    } catch (error) {
      alert("Error connecting to backend.");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="card">
        <h1>🎓 Student Performance Predictor</h1>

        <div className="form-grid">

          <select name="gender" onChange={handleChange}>
            <option value="">Select Gender</option>
            <option>male</option>
            <option>female</option>
          </select>

          <input
            type="text"
            name="race/ethnicity"
            placeholder="race/ethnicity (e.g., group B)"
            onChange={handleChange}
          />

          <input
            type="text"
            name="parental level of education"
            placeholder="parental level of education"
            onChange={handleChange}
          />

          <select name="lunch" onChange={handleChange}>
            <option value="">Select Lunch Type</option>
            <option>standard</option>
            <option>free/reduced</option>
          </select>

          <select name="test preparation course" onChange={handleChange}>
            <option value="">Test Preparation</option>
            <option>completed</option>
            <option>none</option>
          </select>

          <input
            type="number"
            name="reading score"
            placeholder="reading score"
            onChange={handleChange}
          />

          <input
            type="number"
            name="writing score"
            placeholder="writing score"
            onChange={handleChange}
          />
        </div>

        <button onClick={handleSubmit} disabled={loading}>
          {loading ? "Predicting..." : "Predict Score"}
        </button>

        {prediction && (
          <div className="result">
            Predicted Math Score
            <span>{prediction}</span>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;