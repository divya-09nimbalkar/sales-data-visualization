import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "bmw_raw.csv")
processed_path = os.path.join(BASE_DIR, "data", "bmw_processed.csv")

df = pd.read_csv(raw_path)

df["Revenue"] = df["Price_USD"] * df["Sales_Volume"]       # Feature Engineering

df.to_csv(processed_path, index=False)

print("Feature Engineering Completed & Processed File Saved Successfully!")
