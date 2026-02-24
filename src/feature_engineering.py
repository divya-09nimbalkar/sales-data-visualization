import pandas as pd
<<<<<<< HEAD

# Load raw data
df = pd.read_csv(r"C:\Users\HP\Downloads\NIT_DATA_SCIENCE\project_data_visualiation\src\bmw_raw.csv")

# Feature Engineering
df["Revenue"] = df["Price_USD"] * df["Sales_Volume"]

# Save processed dataset
df.to_csv(r"C:\Users\HP\Downloads\NIT_DATA_SCIENCE\project_data_visualiation\src\bmw_raw.csv", index=False)

print("Feature Engineering Completed & Processed File Saved Successfully!")
=======
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "bmw_raw.csv")
processed_path = os.path.join(BASE_DIR, "data", "bmw_processed.csv")

df = pd.read_csv(raw_path)

df["Revenue"] = df["Price_USD"] * df["Sales_Volume"]       # Feature Engineering

df.to_csv(processed_path, index=False)

print("Feature Engineering Completed & Processed File Saved Successfully!")
>>>>>>> 4ccc93b427ec77755189a7f4225955dcb36fa408
