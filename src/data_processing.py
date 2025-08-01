import pandas as pd
import numpy as np
import os
from datetime import datetime

def load_and_clean_data(filepath):
    """
    Load and clean the raw Brent oil price data
    """
    print(f"Loading data from: {filepath}")
    # Load data
    try:
        df = pd.read_csv(filepath)
        
        # Check if we have the expected columns
        if 'Date' not in df.columns:
            # Try to find date column case-insensitively
            date_col = [col for col in df.columns if col.lower() == 'date']
            if date_col:
                df = df.rename(columns={date_col[0]: 'Date'})
            else:
                raise ValueError("No 'Date' column found in the data")
        
        if 'Price' not in df.columns:
            # Try to find price column case-insensitively
            price_col = [col for col in df.columns if col.lower() in ['price', 'value', 'close']]
            if price_col:
                df = df.rename(columns={price_col[0]: 'Price'})
            else:
                raise ValueError("No 'Price' column found in the data")

        print(f"Original data shape: {df.shape}")
        
        # Handle date formatting - specify format to avoid warning
        print("Processing dates...")
        try:
            # First try with day-first format
            df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')
            # For any remaining NaNs, try other common formats
            if df['Date'].isna().any():
                df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
        except:
            # Fallback to automatic parsing if format doesn't match
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Drop rows with invalid dates
        df = df.dropna(subset=['Date'])
        
        # Sort by date and set as index
        df = df.sort_values('Date').set_index('Date')
        print(f"Date range: {df.index.min()} to {df.index.max()}")
        
        # Handle missing values
        print(f"Missing values before cleaning: {df['Price'].isna().sum()}")
        df['Price'] = df['Price'].interpolate(method='time')
        df = df.dropna(subset=['Price'])
        print(f"Missing values after cleaning: {df['Price'].isna().sum()}")
        print(f"Final data shape: {df.shape}")
        
        return df
    
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def calculate_daily_returns(data):
    """
    Calculate daily price returns
    """
    print("Calculating daily returns...")
    data['daily_return'] = data['Price'].pct_change() * 100
    return data

def calculate_volatility(data, window=30):
    """
    Calculate rolling volatility
    """
    print(f"Calculating {window}-day rolling volatility...")
    data['volatility'] = data['daily_return'].rolling(window=window).std()
    return data

def save_processed_data(data, output_path):
    """
    Save processed data to CSV
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path)
        print(f"Processed data saved to: {output_path}")
    except Exception as e:
        print(f"Error saving data: {str(e)}")

def main():
    """Test the data processing functions when run directly"""
    print("=== Brent Oil Price Data Processing ===")
    
    # Path configuration
    raw_data_path = '../data/raw/BrentOilPrices.csv'
    processed_data_path = '../data/processed/brent_clean.csv'
    
    # Load and clean data
    price_data = load_and_clean_data(raw_data_path)
    
    if price_data is not None:
        # Calculate additional metrics
        price_data = calculate_daily_returns(price_data)
        price_data = calculate_volatility(price_data)
        
        # Show sample of processed data
        print("\nSample of processed price data:")
        print(price_data.head())
        
        # Save processed data
        save_processed_data(price_data, processed_data_path)
        
        # Basic statistics
        print("\nBasic Statistics:")
        print(price_data['Price'].describe())
    else:
        print("Data processing failed. Please check the input file.")

if __name__ == "__main__":
    main()