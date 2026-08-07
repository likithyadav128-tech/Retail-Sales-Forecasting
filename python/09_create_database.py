import pandas as pd
import sqlite3

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\processed_sales.csv")

conn = sqlite3.connect(
    r"C:\Users\likit\OneDrive\Documents\Retail-Sales-Forecasting\dataset\retail_sales.db"
)

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("SQLite database created successfully!")