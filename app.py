import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="BMW Sales Dashboard", layout="wide")

try:
    df = pd.read_csv("data/bmw_processed.csv")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

st.title("🚗 BMW Global Sales Executive Dashboard")

st.sidebar.header("🔎 Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

model_filter = st.sidebar.multiselect(
    "Select Model",
    options=sorted(df["Model"].unique()),
    default=sorted(df["Model"].unique())
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Model"].isin(model_filter))
]

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"${filtered_df['Revenue'].sum():,.0f}")
col2.metric("🚘 Total Sales", f"{filtered_df['Sales_Volume'].sum():,}")
col3.metric("🏷 Avg Price", f"${filtered_df['Price_USD'].mean():,.0f}")

st.markdown("---")

st.subheader("📊 Revenue by Region")

region_rev = filtered_df.groupby("Region")["Revenue"].sum().sort_values()

fig1, ax1 = plt.subplots(figsize=(8, 4))
region_rev.plot(kind="barh", ax=ax1)
ax1.set_xlabel("Revenue")
ax1.set_ylabel("Region")
st.pyplot(fig1)

st.subheader("🚗 Sales Volume by Model")

model_sales = filtered_df.groupby("Model")["Sales_Volume"].sum().sort_values()

fig2, ax2 = plt.subplots(figsize=(8, 4))
model_sales.plot(kind="barh", ax=ax2)
ax2.set_xlabel("Sales Volume")
ax2.set_ylabel("Model")
st.pyplot(fig2)

st.subheader("💲 Price Distribution")

fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df["Price_USD"], kde=True, ax=ax3)
ax3.set_xlabel("Price (USD)")
st.pyplot(fig3)


st.subheader("⬇ Download Filtered Data")

st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_bmw_data.csv",
    mime="text/csv"

)
