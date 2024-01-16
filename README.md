**# Sales Data Analysis**

**## Description**

This Python code performs various analyses on sales data to extract insights about sales trends, product performance, store performance, and price correlations. It generates CSV files with summary statistics and visualizations as PNG files for visual analysis.

**## Installation**

1. **Required Python Version:** 3.6 or higher
2. **External Libraries:**
   - pandas
   - matplotlib
   - shutil
   - statsmodels.tsa.seasonal
   - statsmodels.tsa.arima.model

   Install them using pip:
   ```bash
   pip install pandas matplotlib shutil statsmodels
   ```

**## Usage**

1. Ensure the required libraries are installed.
2. Place the `dabarobjects_data.csv` file in the same directory as the Python script.
3. Run the script using Python:
   ```bash
   python sales_analysis.py
   ```

**## Features**

1. **Total Sales Analysis:**
   - Calculates summary statistics for total sales.
   - Generates a plot of total sales over time.
2. **Date-wise Sales Analysis:**
   - Analyzes sales trends by month and week.
   - Generates plots for monthly and weekly sales trends.
3. **Product-wise Sales Analysis:**
   - Calculates total sales for each product.
   - Generates a bar plot of sales by product.
4. **Store-wise Sales Analysis:**
   - Calculates total sales for each store.
   - Generates a bar plot of sales by store.
5. **Price Analysis:**
   - Calculates the correlation between price and sales.
   - Generates a scatter plot of price vs. sales.
6. **Trend Analysis:**
   - Decomposes sales data into trend, seasonality, and residual components.
   - Generates plots for each component.

**## Output Files**

The script creates the following files in the `output_files` subdirectory:

- CSV files containing summary statistics (e.g., total_sales.csv, monthly_sales.csv, etc.)
- PNG files with visualizations of sales trends and analyses (e.g., total_sales_trend.png, price_vs_sales_scatter.png, etc.)

**## Contributing**

- Follow PEP 8 style guidelines for code formatting.
- Add test cases to ensure code correctness.
- Submit pull requests for any changes or additions.

**## License**

Apache License 2.0

**## Contact**

kelanisidikat883@gmail.com
