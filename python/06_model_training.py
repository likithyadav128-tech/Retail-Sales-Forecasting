import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\processed_sales.csv")

# Remove unnecessary columns
df = df.drop(["Date"], axis=1)

print(df.dtypes)
X = df.drop("Sales", axis=1)

y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))

joblib.dump(model, r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\models\sales_forecasting_model.pkl")

X_train.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\X_train.csv", index=False)
X_test.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\X_test.csv", index=False)
y_train.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\y_train.csv", index=False)
y_test.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\y_test.csv", index=False)

print("Model saved successfully!")