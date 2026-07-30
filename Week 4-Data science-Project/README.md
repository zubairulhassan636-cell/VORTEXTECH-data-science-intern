# VortexTech Data Science Internship — Week 4 Advanced

## Telecom Customer Churn: Retention Opportunities

This capstone project follows the Week 4 Advanced instructions: raw-data cleaning, exploratory analysis, four key business findings, 5+ polished visualizations, an executive summary, and actionable recommendations.

### Business Question

**Why are customers leaving, which groups are most at risk, and where should a telecom company focus retention efforts?**

### Project Contents

```text
vortextech-datasci-week4/
├── data/
│   ├── telco_customer_churn.csv
│   └── telco_customer_churn_clean.csv   # created after running notebook
├── notebooks/
│   └── vortextech_week4_telco_churn.ipynb
├── reports/
│   └── telco_churn_executive_report.pdf
├── README.md
└── requirements.txt
```

### Dataset

The included dataset is a **synthetic telecom customer churn dataset** created for internship practice. It contains 7,043 unique customers and 21 fields modeled on common telecom churn analysis variables. It contains no real customer information.

For reference, the project structure is inspired by the widely used IBM Telco Customer Churn dataset, whose public schema includes fields such as tenure, contract, internet service, payment method, monthly charges, total charges, and churn. The IBM dataset is documented in public IBM/Databricks materials.

### Main Findings

1. **Early tenure is the biggest risk period:** customers in their first 12 months show about **52.5% churn**, compared with about **6.1%** for customers with 49–72 months of tenure.
2. **Month-to-month contracts are higher risk:** churn is about **29.6%** for month-to-month customers versus about **18.0%** for two-year customers.
3. **Fiber-optic customers have elevated churn:** about **30.5%**, compared with about **21.2%** for DSL customers.
4. **Electronic-check users are higher risk:** about **27.5%** churn, above the rate among automatic bank-transfer/credit-card users.

Additional analysis shows higher churn among customers without technical support and among customers with higher monthly charges.

### Recommendations

- Create a **first-year retention program** with onboarding, proactive check-ins, and early satisfaction monitoring.
- Offer **clear, value-based incentives** to move suitable month-to-month customers toward longer contracts.
- Investigate **fiber customer experience and electronic-check payment friction** before launching targeted retention tests.

### How to Run

1. Install Python 3.10+.
2. Open a terminal in the project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start Jupyter:

```bash
jupyter notebook
```

5. Open:

```text
notebooks/vortextech_week4_telco_churn.ipynb
```

6. Run all cells from top to bottom.

### GitHub Submission

Recommended repository name:

`vortextech-datasci-week4`

Suggested commands:

```bash
git init
git add .
git commit -m "Complete VortexTech Week 4 advanced data science project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

### Notes

The analysis is descriptive. Relationships shown in the charts are **associations, not proof of causation**. Business teams should validate these findings with customer feedback, operational data, and controlled retention experiments.
