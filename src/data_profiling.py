import pandas as pd

def load_data():
    """
    Load BMW dataset from data folder
    """
    df = pd.read_csv("data/bmw_raw.csv")
    return df


def get_basic_info(df):
    """
    Return dataset summary information
    """
    info = {
        "shape": df.shape,
        "missing_values": df.isnull().sum(),
        "description": df.describe(),
        "unique_counts": df.nunique()
    }
    return info
