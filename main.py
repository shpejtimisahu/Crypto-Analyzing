import pandas as pd
import pandas_datareaders_unofficial as pdr
import ta

# Fetch historical Bitcoin price data from Yahoo Finance
df = pdr.DataReader('BTC-USD', data_source='yahoo', start='2022-01-01', end='2022-12-31')

# Calculate technical analysis indicators
df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
df['SMA_50'] = ta.trend.sma_indicator(df['Close'], window=50)

# Detect breakout momentum
df['Breakout'] = (df['Close'] > df['SMA_20']) & (df['Close'].shift() < df['SMA_20'].shift())

# Generate alerts for breakout moments
breakout_alerts = df[df['Breakout']]
for date, _ in breakout_alerts.iterrows():
    print(f"Breakout detected on {date}")

# Print the DataFrame with breakout moments and technical indicators
print(df)
