# Predictive Analytics Using Historical Data

## Project Overview
This project focuses on predictive analytics using historical sales data.  
A machine learning model is built to forecast future sales trends using Linear Regression.

The project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Data visualization
- Predictive modeling
- Model evaluation
- Future sales forecasting
<a href="https://github.com/AkulaNavyaSri08/Predictive-Analysis/blob/main/predictive_analysis.py">predictive analysis</a>
---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- OpenPyXL

---

# Dataset Information

The dataset contains historical sales data with the following columns:

| Column Name | Description |
|-------------|-------------|
| Date | Sales date |
| Month | Month name |
| Product | Product category |
| Region | Sales region |
| Units Sold | Number of units sold |
| Unit Price | Price per unit |
| Revenue | Total sales revenue |

---

# Project Workflow

1. Import libraries
2. Load dataset
3. Clean and preprocess data
4. Perform Exploratory Data Analysis
5. Create visualizations
6. Train Linear Regression model
7. Predict future revenue
8. Evaluate model accuracy
9. Save trained model

---

# Machine Learning Model

The project uses:

## Linear Regression

The regression equation:

y = β₀ + β₁x

Where:
- y = Predicted Revenue
- x = Month Number
- β₀ = Intercept
- β₁ = Coefficient

---

# Visualizations Included

- Sales Trend Over Time
- Revenue by Product
- Revenue by Region
- Monthly Revenue Analysis
- Actual vs Predicted Revenue

---

# Model Evaluation Metrics

The model is evaluated using:

- Mean Squared Error (MSE)
- R² Score

---
<a href="https://github.com/AkulaNavyaSri08/Predictive-Analysis/blob/main/sales_historical_data_sample.xlsx">dataset view</a>
# Project Structure
<img width="1280" height="692" alt="month by revenue" src="https://github.com/user-attachments/assets/243d5a8b-23bc-4891-9da6-bc6153350d7c" />
<img width="1280" height="692" alt="prediction chart" src="https://github.com/user-attachments/assets/a98adff6-a80d-433b-9f5e-e2b9dbc3a305" />
<img width="800" height="646" alt="product by revenue" src="https://github.com/user-attachments/assets/8e3c2d70-f98e-4d43-9e86-a01d32a4481b" />
<img width="1280" height="692" alt="revenue by region" src="https://github.com/user-attachments/assets/0c01fe97-1ef0-4e71-b5e0-b584eeb47ab9" />
<img width="1200" height="600" alt="Sales trends" src="https://github.com/user-attachments/assets/4b1187db-7543-47c3-8eaa-e61c18f0bc28" />

```text
Predictive_Analytics_Project/
│
├── predictive_analysis.py
├── sales_historical_data_sample.xlsx
├── sales_prediction_model.pkl
├── README.md
│
└── charts/
    ├── Sales trend.png
    ├── product byrevenue.png
    ├── region by revenue.png
    ├── month by revenue.png
    └── prediction charts.png
