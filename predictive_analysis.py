# ============================================
# PREDICTIVE ANALYTICS USING HISTORICAL DATA
# ============================================

# STEP 1: IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# ============================================
# STEP 2: LOAD DATASET
# ============================================

df = pd.read_excel("sales_historical_data_sample.xlsx")

# Display first 5 rows
print("\nFIRST 5 ROWS OF DATASET")
print(df.head())

# ============================================
# STEP 3: DATASET INFORMATION
# ============================================

print("\nDATASET INFORMATION")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

# ============================================
# STEP 4: DATA CLEANING
# ============================================

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

print("\nDATA CLEANING COMPLETED")

# ============================================
# STEP 5: EXPLORATORY DATA ANALYSIS
# ============================================

# Monthly Revenue
monthly_sales = df.groupby('Month')['Revenue'].sum()

print("\nMONTHLY REVENUE")
print(monthly_sales)

# Product Revenue
product_sales = df.groupby('Product')['Revenue'].sum()

print("\nPRODUCT REVENUE")
print(product_sales)

# Region Revenue
region_sales = df.groupby('Region')['Revenue'].sum()

print("\nREGION REVENUE")
print(region_sales)

# ============================================
# STEP 6: VISUALIZATIONS
# ============================================

# 1. Sales Trend Over Time

daily_sales = df.groupby('Date')['Revenue'].sum()

plt.figure(figsize=(12,6))
plt.plot(daily_sales)

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.show()

# ============================================

# 2. Revenue by Product

plt.figure(figsize=(8,5))

product_sales.plot(kind='bar')

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()

# ============================================

# 3. Revenue by Region

plt.figure(figsize=(7,7))

region_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Revenue by Region")
plt.ylabel("")

plt.show()

# ============================================

# 4. Monthly Revenue Chart

plt.figure(figsize=(10,5))

monthly_sales.plot(kind='bar')

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()

# ============================================
# STEP 7: FEATURE ENGINEERING
# ============================================

# Create numerical month column
df['Month_Number'] = df['Date'].dt.month

print("\nFEATURE ENGINEERING COMPLETED")
print(df[['Date', 'Month_Number']].head())

# ============================================
# STEP 8: PREPARE DATA FOR MODEL
# ============================================

X = df[['Month_Number']]
y = df['Revenue']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ============================================
# STEP 9: TRAIN MACHINE LEARNING MODEL
# ============================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nMODEL TRAINING COMPLETED")

# ============================================
# STEP 10: MAKE PREDICTIONS
# ============================================

predictions = model.predict(X_test)

print("\nPREDICTIONS")
print(predictions[:10])

# ============================================
# STEP 11: MODEL EVALUATION
# ============================================

mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMODEL EVALUATION")

print("Mean Squared Error:", mse)

print("R2 Score:", r2)

# ============================================
# STEP 12: ACTUAL VS PREDICTED VISUALIZATION
# ============================================

plt.figure(figsize=(8,5))

plt.scatter(X_test, y_test, label="Actual Values")

plt.plot(X_test, predictions, color='red', label="Predicted Values")

plt.title("Actual vs Predicted Revenue")

plt.xlabel("Month Number")

plt.ylabel("Revenue")

plt.legend()

plt.show()

# ============================================
# STEP 13: FUTURE PREDICTIONS
# ============================================

future_months = pd.DataFrame({
    'Month_Number': [7, 8, 9, 10, 11, 12]
})

future_predictions = model.predict(future_months)

print("\nFUTURE SALES PREDICTIONS")

for month, prediction in zip(
    future_months['Month_Number'],
    future_predictions
):
    print(f"Month {month}: Predicted Revenue = {prediction:.2f}")

# ============================================
# STEP 14: SAVE MODEL
# ============================================

with open("sales_prediction_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nMODEL SAVED SUCCESSFULLY")

# ============================================
# STEP 15: PROJECT COMPLETED
# ============================================

print("\nPREDICTIVE ANALYTICS PROJECT COMPLETED SUCCESSFULLY")