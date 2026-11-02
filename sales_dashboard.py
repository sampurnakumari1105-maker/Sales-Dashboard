import pandas as pd
import matplotlib.pyplot as plt

# Load sales dataset
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("SALES DATA")
print(df.head())

# Dataset information
print("\nDATASET INFORMATION")
print(df.info())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Convert Date into datetime format
df['Date'] = pd.to_datetime(df['Date'])

print("\nDataset loaded successfully!")

# =================================
# SALES ANALYSIS
# =================================

# 1. Total Revenue
total_revenue = df['Revenue'].sum()
print("\nTotal Revenue:", total_revenue)

# 2. Total Orders
total_orders = df['Order_ID'].nunique()
print("Total Orders:", total_orders)

# 3. Total Quantity Sold
total_quantity = df['Quantity'].sum()
print("Total Quantity Sold:", total_quantity)

# 4. Average Order Value
average_order = total_revenue / total_orders
print("Average Order Value:", round(average_order, 2))


# =================================
# TOP SELLING PRODUCTS
# =================================

product_sales = df.groupby('Product')['Quantity'].sum()

top_products = product_sales.sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products)


# =================================
# MONTHLY REVENUE
# =================================

df['Month'] = df['Date'].dt.month_name()

monthly_sales = df.groupby('Month')['Revenue'].sum()

print("\nMonthly Revenue:")
print(monthly_sales)

# =================================
# DATA VISUALIZATION
# =================================

import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# TOP 5 SELLING PRODUCTS
top_5 = product_sales.sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6))

plt.bar(top_5.index, top_5.values)

plt.title("Top 5 Selling Products")
plt.xlabel("Products")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("charts/top_products.png")
plt.show()

# MONTHLY REVENUE TREND

monthly_revenue = df.groupby(
    df['Date'].dt.to_period('M')
)['Revenue'].sum()

monthly_revenue.index = monthly_revenue.index.astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker='o',
    linewidth=2
)

plt.title("Monthly Revenue Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

plt.savefig("charts/monthly_revenue.png")
plt.show()

# =================================
# SALES INSIGHTS
# =================================

import calendar

print("\n========== SALES INSIGHTS ==========")

# Product-wise analysis
product_summary = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Revenue=('Revenue', 'sum')
)

# Best selling product
best_product = product_summary['Total_Quantity'].idxmax()

# Highest revenue product
highest_revenue_product = product_summary['Total_Revenue'].idxmax()

# Monthly revenue analysis
monthly_revenue = df.groupby(
    df['Date'].dt.month
)['Revenue'].sum()

# Best performing month
best_month_number = monthly_revenue.idxmax()
best_month = calendar.month_name[best_month_number]

print("Best Selling Product:", best_product)

print("Highest Revenue Product:", highest_revenue_product)

print("Best Revenue Month:", best_month)

print("\nProduct Performance:")
print(product_summary.sort_values(
    by='Total_Revenue',
    ascending=False
))

print("\n===================================")

