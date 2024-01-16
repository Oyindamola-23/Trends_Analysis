import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import shutil
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

# Load the data with correct column names and date parsing
df = pd.read_csv('dabarobjects_data.csv', parse_dates=['date of sales'], dayfirst=True)

# Explore the structure of the data
print(df.info())

# 1. Total Sales Analysis
total_sales = df['total sales']
 ## Save summary to CSV
total_sales.describe().to_csv('total_sales_summary.csv')
 ## Save data to CSV
total_sales.to_csv('total_sales.csv', index=False)
 ##Print the Analysis
print("Total Sales Analysis complete.")

plt.figure(figsize=(10, 6))
plt.plot(df['date of sales'], df['total sales'], label='Total Sales')
plt.title('Total Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
 ## Save plot as PNG
plt.savefig('total_sales_trend.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('total_sales_trend.png', 'output_files/total_sales_trend.png')
 ## Close the plot window
plt.close()

# 2. Date of Sales Analysis - Monthly Trends
df['month'] = df['date of sales'].dt.to_period('M')
monthly_sales = df.groupby('month')['total sales'].sum()
 ## Save summary to CSV
monthly_sales.to_csv('monthly_sales_summary.csv')
 ## Save data to CSV
monthly_sales.to_csv('monthly_sales.csv', header=['Total Sales'])
 ##Print the Analysis
print("Monthly Sales Analysis complete.")

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', linestyle='-', label='Monthly Sales')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend()
 ## Save plot as PNG
plt.savefig('monthly_sales_trend.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('monthly_sales_trend.png', 'output_files/monthly_sales_trend.png')
 ## Close the plot window
plt.close()

# 3. Date of Sales Analysis - Weekly Trends
df['week'] = df['date of sales'].dt.to_period('W')
weekly_sales = df.groupby('week')['total sales'].sum()
 ## Save summary to CSV
weekly_sales.to_csv('weekly_sales_summary.csv')
 ## Save data to CSV
weekly_sales.to_csv('weekly_sales.csv', header=['Total Sales'])
 ##Print the Analysis
print("Weekly Sales Analysis complete.")

plt.figure(figsize=(10, 6))
plt.plot(weekly_sales.index.astype(str), weekly_sales.values, marker='o', linestyle='-', label='Weekly Sales')
plt.title('Weekly Sales Trend')
plt.xlabel('Week')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend()
 ## Save plot as PNG
plt.savefig('weekly_sales_trend.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('weekly_sales_trend.png', 'output_files/weekly_sales_trend.png')
 ## Close the plot window
plt.close()

# 4. ProductId Analysis (Trends for specific products)
product_groups = df.groupby('productId')['total sales'].sum()
 ## Save summary to CSV
product_groups.to_csv('product_wise_sales_summary.csv')
 ## Save data to CSV
product_groups.to_csv('product_wise_sales.csv', header=['Total Sales'])
print("Product Wise Sales Analysis complete.")

plt.figure(figsize=(10, 6))
plt.bar(product_groups.index, product_groups.values, color='skyblue', label='Total Sales by Product')
plt.title('Product-wise Sales Analysis')
plt.xlabel('Product ID')
plt.ylabel('Total Sales')
plt.legend()
 ## Save plot as PNG
plt.savefig('product_wise_sales_analysis.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('product_wise_sales_analysis.png', 'output_files/product_wise_sales_analysis.png')
 ## Close the plot window
plt.close()

# 5. StoreId Analysis (Trends for specific stores)
store_groups = df.groupby('storeId')['total sales'].sum()
 ## Save summary to CSV
store_groups.to_csv('store_wise_sales_summary.csv')
 ## Save data to CSV
store_groups.to_csv('store_wise_sales.csv', header=['Total Sales'])
 ##Print the Analysis
print("Store Wise Sales Analysis complete.")

plt.figure(figsize=(10, 6))
plt.bar(store_groups.index, store_groups.values, color='lightcoral', label='Total Sales by Store')
plt.title('Store-wise Sales Analysis')
plt.xlabel('Store ID')
plt.ylabel('Total Sales')
plt.legend()
 ## Save plot as PNG
plt.savefig('store_wise_sales_analysis.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('store_wise_sales_analysis.png', 'output_files/store_wise_sales_analysis.png')
 ## Close the plot window
plt.close()

# 6. Price Analysis (Relationship between price and sales)
price_vs_sales = df[['Price in Naira', 'total sales']]
 ## Save correlation to CSV
price_vs_sales.corr().to_csv('price_vs_sales_correlation.csv')
 ##Print the Analysis
print("Price Vs Sales Analysis complete.")

plt.scatter(df['Price in Naira'], df['total sales'], alpha=0.5)
plt.title('Price vs Total Sales')
plt.xlabel('Price in Naira')
plt.ylabel('Total Sales')
 ## Save plot as PNG
plt.savefig('price_vs_sales_scatter.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('price_vs_sales_scatter.png', 'output_files/price_vs_sales_scatter.png')
 ## Close the plot window
plt.close()

# 7. Date-wise Analysis
 ## Use 'date of sales' as the category
df['category'] = df['date of sales']
date_groups = df.groupby('category')['total sales'].sum()
 ## Save summary to CSV
date_groups.to_csv('date_wise_sales_summary.csv')
 ## Save data to CSV
date_groups.to_csv('date_wise_sales.csv', header=['Total Sales'])
 ##Print the Analysis
print("Date Wise Sales Summary complete.")

plt.figure(figsize=(10, 6))
plt.bar(date_groups.index, date_groups.values, color='purple', label='Total Sales by Date')
plt.title('Date-wise Sales Analysis')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
 ## Save plot as PNG
plt.savefig('date_wise_sales_analysis.png')
plt.show()
 ## Move the PNG file to the output directory
shutil.move('date_wise_sales_analysis.png', 'output_files/date_wise_sales_analysis.png')
 ## Close the plot window
plt.close()

# Calculate total price per store ID
total_price_per_store = df.groupby('storeId')['Price in Naira'].sum()

# Calculate total price per product ID
total_price_per_product = df.groupby('productId')['Price in Naira'].sum()

# Calculate total price per week
df['week'] = df['date of sales'].dt.isocalendar().week
total_price_per_week = df.groupby('week')['Price in Naira'].sum()

# Calculate total price per month
df['month'] = df['date of sales'].dt.to_period('M')
total_price_per_month = df.groupby('month')['Price in Naira'].sum()

# Trend analysis
result = seasonal_decompose(df['Price in Naira'], model='additive', period=12)

# Create a folder for saving files
output_folder = 'output_files'
os.makedirs(output_folder, exist_ok=True)

# Save CSV files
total_price_per_store.to_csv(os.path.join(output_folder, 'total_price_per_store.csv'), header=True)
total_price_per_product.to_csv(os.path.join(output_folder, 'total_price_per_product.csv'), header=True)
total_price_per_week.to_csv(os.path.join(output_folder, 'total_price_per_week.csv'), header=True)
total_price_per_month.to_csv(os.path.join(output_folder, 'total_price_per_month.csv'), header=True)

# Plot and save PNG files for total price per store ID
plt.figure(figsize=(10, 6))
total_price_per_store.plot(kind='bar', color='blue')
plt.title('Total Price in Naira per Store ID')
plt.xlabel('Store ID')
plt.ylabel('Total Price in Naira')
plt.savefig('output_files/total_price_per_store.png')
plt.close()

# Plot and save PNG files for total price per product ID
plt.figure(figsize=(10, 6))
total_price_per_product.plot(kind='bar', color='green')
plt.title('Total Price in Naira per Product ID')
plt.xlabel('Product ID')
plt.ylabel('Total Price in Naira')
plt.savefig('output_files/total_price_per_product.png')
plt.close()

# Plot and save PNG files for total price per week
plt.figure(figsize=(12, 6))
total_price_per_week.plot(kind='line', marker='o', color='orange')
plt.title('Total Price in Naira per Week')
plt.xlabel('Week')
plt.ylabel('Total Price in Naira')
plt.savefig('output_files/total_price_per_week.png')
plt.close()

# Plot and save PNG files for total price per month
plt.figure(figsize=(12, 6))
total_price_per_month.plot(kind='line', marker='o', color='red')
plt.title('Total Price in Naira per Month')
plt.xlabel('Month')
plt.ylabel('Total Price in Naira')
plt.savefig('output_files/total_price_per_month.png')
plt.close()

print("PNG files saved to output_files folder")

# Save PNG file
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(df['date of sales'], df['Price in Naira'], label='Original')
plt.legend()
plt.title('Original Time Series')

plt.subplot(4, 1, 2)
plt.plot(df['date of sales'], result.trend, label='Trend')
plt.legend()
plt.title('Trend Component')

plt.subplot(4, 1, 3)
plt.plot(df['date of sales'], result.seasonal, label='Seasonality')
plt.legend()
plt.title('Seasonality Component')

plt.subplot(4, 1, 4)
plt.plot(df['date of sales'], result.resid, label='Residuals')
plt.legend()
plt.title('Residuals')

plt.tight_layout()

# Save PNG file
png_output_path = os.path.join(output_folder, 'trend_analysis_plots.png')
plt.savefig(png_output_path)
plt.close()

print(f"Files saved to {output_folder}")

print("All analyses completed.")

# Move all CSV files to the output directory
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
for csv_file in csv_files:
    shutil.move(csv_file, f'output_files/{csv_file}')

print("CSV files moved to the output directory.")
