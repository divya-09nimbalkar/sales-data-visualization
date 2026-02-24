import pandas as pd

# Load dataset
df = pd.read_csv("data/bmw_raw.csv")

print("----- FIRST 5 ROWS -----")
print(df.head())

print("\n----- DATASET INFO -----")
print(df.info())

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())

print("\n----- UNIQUE VALUES PER COLUMN -----")
for col in df.columns:
    print(f"{col} : {df[col].nunique()}")
