import pandas as pd
import numpy as np
import ruptures as rpt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import os

# Create directories if they don't exist
os.makedirs('../reports/figures', exist_ok=True)

# 1. Stationarity Test Function
def test_stationarity(series, window=365):
    """
    Test for stationarity using Dickey-Fuller test
    """
    # Calculate rolling statistics
    rolmean = series.rolling(window=window).mean()
    rolstd = series.rolling(window=window).std()
    
    # Plot rolling statistics
    plt.figure(figsize=(12, 6))
    orig = plt.plot(series, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.savefig('../reports/figures/rolling_stats.png')
    plt.show()
    
    # Perform Dickey-Fuller test
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(series, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], 
                       index=['Test Statistic','p-value','#Lags Used',
                              'Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput[f'Critical Value ({key})'] = value
    print(dfoutput)
    return dfoutput

# 2. Time Series Decomposition
def decompose_series(series, period=365):
    """
    Decompose time series into trend, seasonal, and residual components
    """
    decomposition = seasonal_decompose(series.interpolate(), period=period)
    
    # Plot decomposition
    plt.figure(figsize=(12, 8))
    decomposition.plot()
    plt.savefig('../reports/figures/decomposition.png')
    plt.show()
    return decomposition

# 3. Change Point Detection
def detect_changepoints(series, pen=10, model="rbf"):
    """
    Detect change points in time series using Pelt algorithm
    """
    # Convert to numpy array
    signal = series.values.reshape(-1, 1)
    
    # Detect change points
    algo = rpt.Pelt(model=model).fit(signal)
    change_indices = algo.predict(pen=pen)
    
    # Convert indices to dates
    change_dates = series.index[change_indices[:-1]]
    return change_dates

# 4. Visualization Function
def plot_price_with_changepoints(price_series, change_dates):
    """
    Plot price series with vertical lines at change points
    """
    plt.figure(figsize=(14, 7))
    price_series.plot()
    for cp in change_dates:
        plt.axvline(x=cp, color='red', linestyle='--', alpha=0.7, 
                   label=f'Change Point: {cp.strftime("%Y-%m-%d")}')
    plt.title('Brent Oil Prices with Detected Change Points')
    plt.ylabel('Price (USD/barrel)')
    plt.grid(True)
    plt.legend()
    plt.savefig('../reports/figures/price_with_change_points.png')
    plt.show()

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    print("=== Brent Oil Price Analysis ===")
    
    # Load processed data
    try:
        price_data = pd.read_csv('../data/processed/brent_clean.csv', 
                                parse_dates=['Date'], 
                                index_col='Date')
        print("Data loaded successfully. Shape:", price_data.shape)
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()

    # 1. Stationarity Analysis
    print("\n1. Running Stationarity Test...")
    stationarity_results = test_stationarity(price_data['Price'].dropna())
    stationarity_results.to_csv('../reports/stationarity_test_results.csv')

    # 2. Time Series Decomposition
    print("\n2. Decomposing Time Series...")
    decomposition = decompose_series(price_data['Price'])

    # 3. Change Point Detection
    print("\n3. Detecting Change Points...")
    change_dates = detect_changepoints(price_data['Price'], pen=15)
    print(f"Detected {len(change_dates)} change points:")
    for i, date in enumerate(change_dates, 1):
        print(f"{i}. {date.strftime('%Y-%m-%d')}")
    
    # Save change points
    pd.DataFrame({'change_date': change_dates}).to_csv('../reports/change_points.csv', index=False)

    # 4. Visualize Results
    print("\n4. Generating Visualizations...")
    plot_price_with_changepoints(price_data['Price'], change_dates)
    
    print("\n=== Analysis Complete ===")
    print("Outputs saved to:")
    print("- ../reports/figures/")
    print("- ../reports/change_points.csv")
    print("- ../reports/stationarity_test_results.csv")