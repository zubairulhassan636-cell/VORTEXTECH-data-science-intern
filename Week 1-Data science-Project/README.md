# Week 1 - Data Cleaning & Visualization

A small project focused on basic **Data Cleaning** and **Visualization** using a sales dataset. The goal is to clean the raw dataset and explore it through simple charts.

## 📌 Project Overview

In this notebook, the `sales_data.csv` dataset is loaded and:
- Basic dataset info and summary statistics are reviewed
- Missing values and duplicate rows are checked/handled
- Date columns are converted to proper `datetime` format
- A few basic visualizations (Bar Chart, Histogram, Line Chart) are created

## 🗂️ Project Structure

```
├── Week1_Data_Cleaning_Visualization.ipynb   # Main notebook
├── sales_data.csv                             # Dataset (required to run)
└── README.md
```

## 🛠️ Tech Stack

- **Python 3**
- **pandas** – data loading, cleaning
- **matplotlib** – plotting
- **seaborn** – visualization support

## 📊 Steps Performed

1. **Data Loading** – Loaded `sales_data.csv` using pandas
2. **Dataset Info** – Reviewed the dataset overview using `df.info()` and `df.describe()`
3. **Missing Values & Duplicates**
   - Counted missing values per column (`isnull().sum()`)
   - Removed duplicate rows (`drop_duplicates()`)
   - Converted date-related columns using `pd.to_datetime()`
4. **Visualizations**
   - **Bar Chart** for a categorical column
   - **Histogram** for a numeric column
   - **Line Chart** comparing two numeric columns

## ▶️ How to Run


1. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```

2. Place the `sales_data.csv` file in the same folder as the notebook.

3. Run the notebook:
   ```bash
   jupyter notebook Week1_Data_Cleaning_Visualization.ipynb
   ```

## 📈 Sample Outputs

After running the notebook, you will get the following charts:
- Category-wise counts (Bar Chart)
- Distribution of a numeric column (Histogram)
- Trend line chart

## 📝 Notes

- The dataset file must be named exactly `sales_data.csv`, otherwise the file path needs to be updated.
- This project is a beginner-level exercise designed to teach Data Cleaning and basic EDA (Exploratory Data Analysis).

## 👤 Author

**Zubair** — BS Data Science Student
