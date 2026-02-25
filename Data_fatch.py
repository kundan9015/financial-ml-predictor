import yfinance as yf
import pandas as pd

symbol = "RELIANCE.NS"   # change later to BTC-USD if needed

# download data
data = yf.download(symbol, period="5y", interval="1d")

# reset index so Date becomes a column
data.reset_index(inplace=True)

# keep only needed columns
df = data[['Date','Open','High','Low','Close','Volume']]

# remove missing rows
df.dropna(inplace=True)

# save clean dataset
df.to_csv("stock_data.csv", index=False)

print("Clean dataset saved successfully!")
print(df.head())