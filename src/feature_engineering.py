import pandas as pd

# Load dataset
df = pd.read_csv("../data/bmw_raw.csv")

# Create Revenue column
df["Revenue"] = df["Price_USD"] * df["Sales_Volume"]

# Price per Engine Liter
df["Price_per_Liter"] = df["Price_USD"] / df["Engine_Size_L"]

# Sales Growth per Region
df["Sales_Growth"] = df.groupby("Region")["Sales_Volume"].pct_change()

# Save cleaned + engineered dataset
df.to_csv("../data/bmw_cleaned.csv", index=False)

print("Feature Engineering Completed Successfully!")
