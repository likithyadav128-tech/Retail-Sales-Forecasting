import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\cleaned_sales.csv")

# Monthly Sales
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

monthly_sales.plot(figsize=(12,6))

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(True)

plt.show()