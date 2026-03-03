import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("student_data.csv")

label_encoders = {}
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df.drop("math score", axis=1)
y = df["math score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_preds = linear_model.predict(X_test)
linear_score = r2_score(y_test, linear_preds)

# Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
rf_score = r2_score(y_test, rf_preds)

print("Linear Regression R2:", linear_score)
print("Random Forest R2:", rf_score)

# Save best model
if rf_score > linear_score:
    best_model = rf_model
    best_name = "Random Forest"
    best_score = rf_score
else:
    best_model = linear_model
    best_name = "Linear Regression"
    best_score = linear_score

joblib.dump(best_model, "model.pkl")
joblib.dump(label_encoders, "encoders.pkl")
joblib.dump({
    "linear_score": linear_score,
    "rf_score": rf_score,
    "best_model": best_name,
    "best_score": best_score
}, "metrics.pkl")

print("Best model:", best_name)
print("Best score:", best_score)