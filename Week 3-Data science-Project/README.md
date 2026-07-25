# Sales Performance Dashboard

**VortexTech Data Science & Analytics Internship — Week 3 (Intermediate)**

An interactive Streamlit dashboard built on top of a sales transactions dataset
(`sales_data.csv`), letting users filter and explore sales performance across
regions, product categories, and customer segments in real time.

## 📊 What This Dashboard Shows

- **KPI summary cards**: total sales, total orders, total units sold, and average order value for the currently filtered data.
- **Total Sales by Region** — bar chart.
- **Monthly Sales Trend** — line chart showing sales over time.
- **Sales by Product Category & Sales Channel** — grouped bar chart (Matplotlib/Seaborn).
- **Quantity Sold vs Sales Amount** — scatter plot colored by product category.
- **Filtered raw data table** showing every record that matches the current filters.

## 🎛️ Filters

| Filter | Type | Description |
|---|---|---|
| Region | Dropdown | Filter by North / South / East / West (or All) |
| Product Category | Dropdown | Filter by Furniture / Food / Clothing / Electronics (or All) |
| Sales Amount Range | Slider | Restrict to orders within a min–max sales amount |
| Customer Type | Dropdown | Filter by New / Returning customers (or All) |

All charts and the data table update live as filters change.

## 📁 Project Structure

```
vortextech-datasci-week3/
├── dashboard.py       # Streamlit app
├── sales_data.csv     # Dataset
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ▶️ How to Run

1. Clone this repository and move into the project folder:
   ```bash
   git clone <your-repo-url>
   cd vortextech-datasci-week3
   ```

2. (Recommended) create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard:
   ```bash
   streamlit run dashboard.py
   ```

5. Streamlit will automatically open the dashboard in your browser
   (usually at `http://localhost:8501`).

## 🗂️ Dataset

`sales_data.csv` contains 1,000 sales records with the following columns:
`Product_ID`, `Sale_Date`, `Sales_Rep`, `Region`, `Sales_Amount`, `Quantity_Sold`,
`Product_Category`, `Unit_Cost`, `Unit_Price`, `Customer_Type`, `Discount`,
`Payment_Method`, `Sales_Channel`, `Region_and_Sales_Rep`.

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — dashboard framework
- [Pandas](https://pandas.pydata.org/) — data manipulation
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) — visualizations
