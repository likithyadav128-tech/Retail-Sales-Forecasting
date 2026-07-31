import pandas as pd

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\merged_sales.csv")

print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values
df["CompetitionDistance"] = df["CompetitionDistance"].fillna(df["CompetitionDistance"].median())

df["CompetitionOpenSinceMonth"] = df["CompetitionOpenSinceMonth"].fillna(0)

df["CompetitionOpenSinceYear"] = df["CompetitionOpenSinceYear"].fillna(0)

df["Promo2SinceWeek"] = df["Promo2SinceWeek"].fillna(0)

df["Promo2SinceYear"] = df["Promo2SinceYear"].fillna(0)

df["PromoInterval"] = df["PromoInterval"].fillna("None")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\cleaned_sales.csv", index=False)

print("\nData cleaned successfully!")