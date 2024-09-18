import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

sns.set(style="whitegrid")

df = pd.read_excel('sales_data.xlsx')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print(df.head())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)

total_sales = df['Sales'].sum()
print(f'Total Sales Revenue: ${total_sales:.2f}')

total_profit = df['Profit'].sum()
print(f'Total Profit: ${total_profit:.2f}')

df['Year-Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Year-Month').sum()['Sales']

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='blue')
plt.title('Monthly Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_products_by_sales = df.groupby('Product Name').sum()['Sales'].sort_values(ascending=False)
top_10_products_by_sales = top_products_by_sales.head(10)
print('Top 10 Best-Selling Products by Sales:')
print(top_10_products_by_sales)

plt.figure(figsize=(10, 6))
top_10_products_by_sales.plot(kind='bar', color='skyblue')
plt.title('Top 10 Best-Selling Products by Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_products_by_quantity = df.groupby('Product Name').sum()['Quantity'].sort_values(ascending=False)
top_10_products_by_quantity = top_products_by_quantity.head(10)
print('Top 10 Best-Selling Products by Quantity:')
print(top_10_products_by_quantity)

plt.figure(figsize=(10, 6))
top_10_products_by_quantity.plot(kind='bar', color='orange')
plt.title('Top 10 Best-Selling Products by Quantity')
plt.xlabel('Product Name')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

category_sales = df.groupby(['Category', 'Sub-Category']).sum()['Sales'].sort_values(ascending=False)
print('Sales by Category and Sub-Category:')
print(category_sales)

plt.figure(figsize=(10, 6))
category_sales.head(10).plot(kind='bar', color='lightgreen')
plt.title('Top Categories and Sub-Categories by Sales')
plt.xlabel('Category - Sub-Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', palette='coolwarm', s=100)
plt.title('Discount vs Profit by Category')
plt.xlabel('Discount')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.show()

category_profit = df.groupby('Category').sum()['Profit'].sort_values(ascending=False)

plt.figure(figsize=(8, 6))
category_profit.plot(kind='bar', color='purple')
plt.title('Total Profit by Category')
plt.xlabel('Category')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Shipping Cost', y='Profit', hue='Region', palette='Set1', s=100)
plt.title('Shipping Cost vs Profit by Region')
plt.xlabel('Shipping Cost ($)')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.show()

sales_by_region = df.groupby('Region').sum()['Sales'].sort_values(ascending=False)

plt.figure(figsize=(8, 8))
sales_by_region.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Sales Distribution by Region')
plt.ylabel('')
plt.tight_layout()
plt.show()
