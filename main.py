import pandas as pd
import pandas_datareaders_unofficial as pdr
import ta

df = pdr.DataReader('BTC-USD', data_source='yahoo', start='2022-01-01', end='2022-12-31')

df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
df['SMA_50'] = ta.trend.sma_indicator(df['Close'], window=50)

df['Breakout'] = (df['Close'] > df['SMA_20']) & (df['Close'].shift() < df['SMA_20'].shift())
# Alert
breakout_alerts = df[df['Breakout']]
for date, _ in breakout_alerts.iterrows():
    print(f"Breakout detected on {date}")


print(df)

