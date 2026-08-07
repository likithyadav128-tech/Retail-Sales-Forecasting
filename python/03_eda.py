import pandas as pd

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\cleaned_sales.csv")

print(df.describe())

print("\nColumns:\n")
print(df.columns)

print("\nTotal Stores:", df["Store"].nunique())

print("\nTotal Sales:", df["Sales"].sum())

print("\nAverage Sales:", df["Sales"].mean())

print("\nMaximum Sales:", df["Sales"].max())

print("\nMinimum Sales:", df["Sales"].min())