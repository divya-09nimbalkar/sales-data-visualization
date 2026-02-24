import pandas as pd

# Go one folder up (from src to project root)
df = pd.read_csv(r"C:\Users\HP\Downloads\NIT_DATA_SCIENCE\project_data_visualiation\src\bmw_raw.csv")

print("File Loaded Successfully!\n")

print("----- FIRST 5 ROWS -----")
print(df.head())

print("\n----- DATASET INFO -----")
print(df.info())

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())