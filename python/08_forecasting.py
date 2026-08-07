import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\cleaned_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

forecast = df.groupby("Date")["Sales"].sum().rolling(30).mean()

plt.figure(figsize=(12,6))

plt.plot(forecast)

plt.title("30-Day Rolling Sales Forecast")

plt.xlabel("Date")

plt.ylabel("Sales")

plt.grid(True)

plt.show()