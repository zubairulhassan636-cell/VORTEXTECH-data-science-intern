# Week 2 - Exploratory Data Analysis (EDA) on Sales Data

An Exploratory Data Analysis (EDA) project performed on a sales dataset, focused on understanding relationships between numeric features, correlations, and category/region-wise sales patterns.

## 📌 Project Overview

In this notebook, the `sales_data.csv` dataset is analyzed to:
- Inspect dataset shape, data types, missing values, and duplicates
- Generate summary statistics for numeric columns
- Compute and visualize correlations between key numeric features
- Explore relationships between cost, price, quantity, and sales using scatter plots
- Compare average sales performance across product categories and regions

## 🗂️ Project Structure

```
├── Week2_EDA_Sales_Data.ipynb   # Main notebook
├── sales_data.csv                # Dataset (required to run)
└── README.md
```

## 🛠️ Tech Stack

- **Python 3**
- **pandas** – data loading and analysis
- **numpy** – numerical operations
- **matplotlib** – plotting
- **seaborn** – statistical visualizations

## 📊 Steps Performed

1. **Data Loading** – Loaded `sales_data.csv` and checked its shape
2. **Data Quality Checks**
   - Checked missing values (`isnull().sum()`)
   - Checked duplicate rows (`duplicated().sum()`)
   - Reviewed column data types (`dtypes`)
3. **Summary Statistics** – Generated descriptive statistics using `describe()`
4. **Correlation Analysis**
   - Computed correlation matrix for `Sales_Amount`, `Quantity_Sold`, `Unit_Cost`, `Unit_Price`, and `Discount`
   - Visualized correlations using a **heatmap**
5. **Relationship Analysis (Scatter Plots)**
   - Unit Cost vs Unit Price
   - Quantity Sold vs Sales Amount
6. **Category & Region Analysis**
   - Average Sales Amount by **Product Category** (bar plot)
   - Average Sales Amount by **Region** (bar plot)

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd <repo-folder>
   ```

2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. Place the `sales_data.csv` file in the same folder as the notebook.

4. Run the notebook:
   ```bash
   jupyter notebook Week2_EDA_Sales_Data.ipynb
   ```

## 📈 Sample Outputs

Running the notebook produces:
- A correlation heatmap of numeric sales features
- Scatter plots showing cost vs price and quantity vs sales relationships
- Bar charts comparing average sales by product category and region

## 📝 Notes

- The dataset must contain the columns: `Sales_Amount`, `Quantity_Sold`, `Unit_Cost`, `Unit_Price`, `Discount`, `Product_Category`, and `Region` for all analyses to run without errors.
- The dataset file must be named exactly `sales_data.csv`, otherwise the file path needs to be updated.
- This project builds on Week 1's data cleaning work and focuses on deeper exploratory analysis to uncover patterns and relationships in the sales data.

## 👤 Author

**Zubair** — BS Data Science Student
