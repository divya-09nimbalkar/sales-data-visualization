import pandas as pd

# Load raw data
df = pd.read_csv(r"C:\Users\HP\Downloads\NIT_DATA_SCIENCE\project_data_visualiation\src\bmw_raw.csv")

# Feature Engineering
df["Revenue"] = df["Price_USD"] * df["Sales_Volume"]

# Save processed dataset
df.to_csv(r"C:\Users\HP\Downloads\NIT_DATA_SCIENCE\project_data_visualiation\src\bmw_raw.csv", index=False)

print("Feature Engineering Completed & Processed File Saved Successfully!")