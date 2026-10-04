import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("sales_data.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Basic analysis
total_sales = df["Sales"].sum()
total_orders = len(df)
average_sales = df["Sales"].mean()

print("Total Sales:", total_sales)
print("Total Orders:", total_orders)
print("Average Sales:", round(average_sales, 2))

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Product:")
print(product_sales)

# Monthly sales
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Product sales chart
product_sales.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
