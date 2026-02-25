import pandas as pd

def process_data(df):
    """
    Perform feature engineering on the dataset.
    Returns processed dataframe.
    """

    # Example Feature: Revenue
    if "Price_USD" in df.columns and "Sales_Volume" in df.columns:
        df["Revenue"] = df["Price_USD"] * df["Sales_Volume"]

    return df
