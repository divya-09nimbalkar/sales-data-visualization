import pandas as pd

<<<<<<< HEAD
# Go one folder up (from src to project root)
df = pd.read_csv(r"C:\Users\HP\Downloads\NIT_DATA_SCIENCE\project_data_visualiation\src\bmw_raw.csv")

print("File Loaded Successfully!\n")
=======
# Load dataset
df = pd.read_csv("data/bmw_raw.csv")
>>>>>>> 4ccc93b427ec77755189a7f4225955dcb36fa408

print("----- FIRST 5 ROWS -----")
print(df.head())

print("\n----- DATASET INFO -----")
print(df.info())

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\n----- STATISTICAL SUMMARY -----")
<<<<<<< HEAD
print(df.describe())
=======
print(df.describe())

print("\n----- UNIQUE VALUES PER COLUMN -----")
for col in df.columns:
    print(f"{col} : {df[col].nunique()}")
>>>>>>> 4ccc93b427ec77755189a7f4225955dcb36fa408
