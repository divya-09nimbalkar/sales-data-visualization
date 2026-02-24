import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed_path = os.path.join(BASE_DIR, "data", "bmw_processed.csv")

df = pd.read_csv(processed_path)

total_revenue = df["Revenue"].sum()
total_sales = df["Sales_Volume"].sum()
avg_price = df["Price_USD"].mean()
top_model = df.groupby("Model")["Sales_Volume"].sum().idxmax()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()

print("\n----- EXECUTIVE KPI DASHBOARD -----")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Sales Volume: {total_sales:,}")
print(f"Average Price: ${avg_price:,.2f}")
print(f"Top Selling Model: {top_model}")
print(f"Top Region by Revenue: {top_region}")
