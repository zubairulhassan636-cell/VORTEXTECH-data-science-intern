"""
Sales Performance Dashboard
VortexTech Data Science & Analytics Internship - Week 3 (Intermediate)

Interactive Streamlit dashboard to explore the sales dataset with
filters for Region, Product Category, and Sales Amount range.
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
)

sns.set_style("whitegrid")

# ---------------------------------------------------------
# Load data (cached so it isn't re-read on every interaction)
# ---------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")
    df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
    df["Month"] = df["Sale_Date"].dt.to_period("M").astype(str)
    return df


df = load_data()

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.title("📊 Sales Performance Dashboard")
st.markdown(
    "Explore sales performance across regions, product categories, and time. "
    "Use the filters in the sidebar to drill into the data."
)

# ---------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------
st.sidebar.header("🔎 Filters")

# Filter 1: Region (dropdown)
region_options = ["All"] + sorted(df["Region"].unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", region_options)

# Filter 2: Product Category (dropdown)
category_options = ["All"] + sorted(df["Product_Category"].unique().tolist())
selected_category = st.sidebar.selectbox("Select Product Category", category_options)

# Filter 3: Sales Amount (slider - numeric range)
min_amt, max_amt = float(df["Sales_Amount"].min()), float(df["Sales_Amount"].max())
selected_amt_range = st.sidebar.slider(
    "Sales Amount Range ($)",
    min_value=min_amt,
    max_value=max_amt,
    value=(min_amt, max_amt),
)

# Filter 4 (bonus): Customer Type (dropdown)
customer_options = ["All"] + sorted(df["Customer_Type"].unique().tolist())
selected_customer = st.sidebar.selectbox("Select Customer Type", customer_options)

# ---------------------------------------------------------
# Apply filters
# ---------------------------------------------------------
filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Product_Category"] == selected_category]

if selected_customer != "All":
    filtered_df = filtered_df[filtered_df["Customer_Type"] == selected_customer]

filtered_df = filtered_df[
    (filtered_df["Sales_Amount"] >= selected_amt_range[0])
    & (filtered_df["Sales_Amount"] <= selected_amt_range[1])
]

# ---------------------------------------------------------
# KPI summary cards
# ---------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered_df['Sales_Amount'].sum():,.2f}")
col2.metric("Total Orders", f"{len(filtered_df):,}")
col3.metric("Total Units Sold", f"{filtered_df['Quantity_Sold'].sum():,}")
avg_order = filtered_df["Sales_Amount"].mean() if len(filtered_df) else 0
col4.metric("Avg. Order Value", f"${avg_order:,.2f}")

st.divider()

# ---------------------------------------------------------
# Visualization 1: Total sales by Region (bar chart)
# ---------------------------------------------------------
st.subheader("Total Sales by Region")
sales_by_region = filtered_df.groupby("Region")["Sales_Amount"].sum().sort_values(ascending=False)
st.bar_chart(sales_by_region)

# ---------------------------------------------------------
# Visualization 2: Monthly sales trend (line chart)
# ---------------------------------------------------------
st.subheader("Monthly Sales Trend")
sales_by_month = filtered_df.groupby("Month")["Sales_Amount"].sum().sort_index()
st.line_chart(sales_by_month)

# ---------------------------------------------------------
# Visualization 3: Sales by Product Category & Sales Channel (matplotlib)
# ---------------------------------------------------------
st.subheader("Sales by Product Category & Sales Channel")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    data=filtered_df,
    x="Product_Category",
    y="Sales_Amount",
    hue="Sales_Channel",
    estimator=sum,
    errorbar=None,
    ax=ax,
)
ax.set_ylabel("Total Sales ($)")
ax.set_xlabel("Product Category")
st.pyplot(fig)

# ---------------------------------------------------------
# Visualization 4 (bonus): Quantity vs Sales Amount (scatter)
# ---------------------------------------------------------
st.subheader("Quantity Sold vs Sales Amount")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.scatterplot(
    data=filtered_df,
    x="Quantity_Sold",
    y="Sales_Amount",
    hue="Product_Category",
    ax=ax2,
)
st.pyplot(fig2)

st.divider()

# ---------------------------------------------------------
# Filtered raw data table
# ---------------------------------------------------------
st.subheader("Filtered Raw Data")
st.write(f"Showing {len(filtered_df)} of {len(df)} total records")
st.dataframe(filtered_df.drop(columns=["Month"]), use_container_width=True)
