import pandas as pd
df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\cleaned_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month

df["Day"] = df["Date"].dt.day

df["Week"] = df["Date"].dt.isocalendar().week.astype(int)

# Convert categorical columns
categorical_columns = [
    "StoreType",
    "Assortment",
    "StateHoliday",
    "PromoInterval"
]

df = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True
)

df.to_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\processed_sales.csv", index=False)

print("Feature Engineering Completed!")