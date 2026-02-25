import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import pickle
import plotly.graph_objects as go

model = pickle.load(open("model.pkl", "rb"))
feature_columns = pickle.load(open("features.pkl", "rb"))

st.set_page_config(page_title="ML Stock Predictor", layout="wide")
st.title("📈 Financial Market Prediction Dashboard")
st.write("Predict next-day price direction using Machine Learning")

symbol = st.text_input(
    "Enter Stock or Crypto Symbol (Example: RELIANCE.NS, TCS.NS, BTC-USD)",
    "RELIANCE.NS"
)

data = yf.download(symbol, period="6mo", interval="1d")

if len(data) < 60:
    st.warning("Not enough market data to make prediction.")
    st.stop()
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

df = data[['Open','High','Low','Close','Volume']].copy()

df['Return'] = df['Close'].pct_change()

df['MA10'] = df['Close'].rolling(10).mean()
df['MA20'] = df['Close'].rolling(20).mean()
df['MA50'] = df['Close'].rolling(50).mean()
df['MA_Cross'] = (df['MA10'] > df['MA50']).astype(int)
df['Volatility'] = df['Return'].rolling(20).std()
df['Volume_Change'] = df['Volume'].pct_change()
df['Volume_MA20'] = df['Volume'].rolling(20).mean()
df['High_Volume'] = (df['Volume'].values > df['Volume_MA20'].values).astype(int)
df['Price_Change'] = df['Close'].diff()
df['Momentum_5'] = df['Close'] - df['Close'].shift(5)
df['Momentum_10'] = df['Close'] - df['Close'].shift(10)

delta = df['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
rs = gain / loss
df['RSI'] = 100 - (100/(1+rs))
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)


latest = df.iloc[-1:] # takeing last raw of the data rest

latest = latest.reindex(columns=feature_columns, fill_value=0)

prediction = model.predict(latest)[0]
st.subheader("📊 Model Prediction")

if prediction == 1:
    st.success("🟢 BUY Signal → Price likely to go UP tomorrow")
else:
    st.error("🔴 SELL Signal → Price likely to go DOWN tomorrow")

# ---------------- CHART ----------------
st.subheader("Price Chart")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df.index,
    y=df['Close'],
    name="Close Price",
    line=dict(color='cyan')
))

fig.add_trace(go.Scatter(
    x=df.index,
    y=df['MA20'],
    name="MA20",
    line=dict(color='orange')
))

fig.add_trace(go.Scatter(
    x=df.index,
    y=df['MA50'],
    name="MA50",
    line=dict(color='green')
))

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.caption(" Developed by Kundan Kumawat")
