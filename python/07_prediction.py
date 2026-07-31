import pandas as pd
import joblib

model = joblib.load(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\models\sales_forecasting_model.pkl")

X_test = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\X_test.csv")

prediction = model.predict(X_test)

print("First 10 Predictions:\n")

print(prediction[:10])