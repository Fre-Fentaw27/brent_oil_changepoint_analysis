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

## Task 2: Change Point Modeling and Insight Generation

### Overview

This repository contains the analysis for Task 2, focusing on [briefly describe the main goal of the task, e.g., "detecting change points in the Brent crude oil price time series using both frequentist and Bayesian methods"]. The analysis aims to [state the key objectives, e.g., "identify significant shifts in price mean and volatility, quantify their impact, and correlate them with historical events"].

### Data

The analysis uses the Brent crude oil price data from a CSV file located at `[path to data file, e.g., data/processed/brent_clean.csv]`. This dataset has been pre-processed to include:

- **Date:** The date of the observation.
- **Price:** The daily closing price of Brent crude oil.
- **Daily Return:** The daily percentage change in price.
- **Log Return:** The natural logarithm of the daily price returns, used for volatility analysis.

### Methods

The analysis was performed using two distinct methodologies to detect change points:

#### 1. Frequentist Approach (Ruptures)

- **Library:** `ruptures`
- **Algorithm:** We used the [specify algorithm, e.g., "Binary Segmentation with a PELT (Pruned Exact Linear Time) search method"] to detect change points in the [specify data, e.g., "daily price series"]. The model aims to find abrupt changes in the [specify property, e.g., "mean of the time series"].
- **Output:** The result is a set of specific dates where the mean price is hypothesized to have changed.

#### 2. Bayesian Approach (PyMC)

- **Library:** `PyMC`
- **Model:** A Bayesian change point model was constructed to detect shifts in the **volatility** (standard deviation) of the time series.
- **Prior Distributions:**
  - **Change Point (`tau`):** A discrete uniform prior was used, assuming a change could occur at any point in the time series.
  - **Volatilities (`sigma_1`, `sigma_2`):** Half-Normal priors were chosen for the standard deviations before and after the change point, as volatility must be positive.
  - **Mean (`mu_log_return`):** A Normal prior was used for the mean of the log returns, centered around zero.
- **Sampling:** The model was sampled using a hybrid MCMC approach (`Metropolis` for `tau` and `NUTS` for continuous parameters) to find the posterior distributions of the parameters. This allows us to quantify the uncertainty of the change point location and the magnitude of the volatility shift.

### Results

The analysis yielded the following key findings:

- **Rupture Change Points:** A list of dates where significant shifts in the Brent oil price mean were detected.
  - [List the detected dates here, e.g., "1990-08-01 (Gulf War)", "2008-09-15 (Lehman Brothers Collapse)"]
- **Bayesian Change Point:** The most probable date for a significant shift in volatility was identified, along with its posterior probability distribution.
  - **Most Probable Date:** `[Insert date here, e.g., 2008-09-15]`
  - **Volatility Change:** A `[e.g., 150%]` increase in volatility was estimated by comparing the posterior means of `sigma_1` and `sigma_2`.
- **Historical Correlation:** Both methods identified change points that correspond to known historical events that impacted the oil market, such as [list events and their corresponding dates].

## Task 3: Developing an Interactive Dashboard for Data Analysis Results

- Key Features

  - Historical Trends: Display the Brent oil price and volatility over time.

  - Event Highlights: Visualize specific political, economic, or conflict-related events on the time series to show their impact on prices.

  - Interactive Controls: Users can filter data by date range, select specific events, and compare different time periods.

  - Key Indicators: The dashboard presents key metrics, such as average price and volatility changes around detected change points.

  - Responsiveness: The interface is designed to be fully responsive, ensuring a seamless experience on desktop, tablet, and mobile devices.

- Technology Stack

  - Backend: Flask (Python)

  - Serves data via RESTful APIs.

  - Frontend: React.js

  - Builds the interactive user interface.

  - chart Library: [ Recharts, React Chart.js 2]
