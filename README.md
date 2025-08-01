# brent_oil_changepoint_analysis

Change point analysis and statistical modelling of time series data-detecting changes and associating causes on time series data.

# Brent Oil Price Analysis - Task 1

## Project Overview

This project analyzes historical Brent crude oil prices (1987-2022) to identify significant price change events and their impacts. The analysis focuses on time series properties, structural breaks, and key statistical insights.

## Folder Structure

brent_oil_analysis/
├── data/
│ ├── raw/ # Original Brent oil price data
│ └── processed/ # Cleaned and processed data
├── notebooks/
│ ├── 01_data_exploration.ipynb # Initial data analysis
│ ├── 02_time_series_analysis.ipynb # Time series properties
│ ├── 03_change_point_detection.ipynb # Event impact analysis
│ └── 04_generate_report.ipynb # Report generation
├── reports/
│ ├── figures/ # Visualizations
│ ├── change_points.csv # Detected structural breaks
│ └── brent_analysis_report.pdf # Final report
└── src/
├── data_processing.py # Data cleaning functions
└── analysis_functions.py # Analysis functions

## Key Features

1. **Data Processing Pipeline**

   - Cleans and preprocesses raw Brent oil price data
   - Handles missing values and date formatting
   - Calculates daily returns and volatility metrics

2. **Time Series Analysis**

   - Stationarity testing (ADF test)
   - Trend/seasonality decomposition
   - Rolling statistics visualization

3. **Change Point Detection**

   - Identifies significant structural breaks using Pelt algorithm
   - Visualizes price changes with event markers

4. **Reporting**
   - Generates PDF and text reports
   - Includes key statistics and detected events

## How to Run

1. **Prerequisites**
   ```bash
   pip install pandas numpy matplotlib ruptures statsmodels fpdf
   ```
2. **Execution Order**

- Run src/data_processing.py
- Run notebooks in numerical order (01 to 03)
