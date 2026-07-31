import pandas as pd

# Load datasets
train = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\train.csv")
store = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\store.csv")

# Merge datasets
df = pd.merge(train, store, on="Store", how="left")

print(df.head())

# Save merged dataset
df.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\merged_sales.csv", index=False)

print("\nMerged dataset saved successfully!")