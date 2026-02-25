def calculate_kpis(df):
    """
    Calculate executive KPI metrics from dataframe.
    Returns a dictionary of KPI values.
    """

    kpis = {}

    if "Revenue" in df.columns:
        kpis["total_revenue"] = df["Revenue"].sum()
    else:
        kpis["total_revenue"] = 0

    if "Sales_Volume" in df.columns:
        kpis["total_sales"] = df["Sales_Volume"].sum()
    else:
        kpis["total_sales"] = 0

    if "Price_USD" in df.columns:
        kpis["avg_price"] = df["Price_USD"].mean()
    else:
        kpis["avg_price"] = 0

    if "Model" in df.columns and "Sales_Volume" in df.columns:
        kpis["top_model"] = df.groupby("Model")["Sales_Volume"].sum().idxmax()
    else:
        kpis["top_model"] = "N/A"

    if "Region" in df.columns and "Revenue" in df.columns:
        kpis["top_region"] = df.groupby("Region")["Revenue"].sum().idxmax()
    else:
        kpis["top_region"] = "N/A"

    return kpis
