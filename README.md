# 📈 Financial Market Prediction Dashboard

An end-to-end Machine Learning web application that predicts the next-day direction (UP/DOWN) of stocks and cryptocurrencies using technical indicators and a Random Forest classification model.
Link:-https://financial-ml-predictor-ggpmmprxl4znuqbkks7b2m.streamlit.app

---

## 🔍 Problem Statement
Financial markets are highly volatile and difficult to predict.  
This project aims to analyze historical price behavior and technical indicators to generate a **Buy/Sell signal** for the next trading day.

Instead of predicting exact price (which is unreliable), the model predicts **direction**, which is more useful in trading decision making.

---

## 🚀 Features
- Real-time stock & crypto data (Yahoo Finance API)
- Machine Learning-based price direction prediction
- Buy/Sell signal generation
- Interactive price charts
- Moving average trend visualization

---

## 🧠 Machine Learning Approach
The project converts financial time-series data into a supervised classification problem.

**Model:** Random Forest Classifier  
**Evaluation:** Chronological Train-Test Split (Time-Series Aware)

The model avoids data leakage by training only on past data and testing on future data.

---

## 📊 Technical Indicators Used
- Moving Averages (MA10, MA20, MA50)
- Moving Average Crossover (Trend Signal)
- Volatility (Rolling Standard Deviation)
- Volume Activity Signals
- RSI (Relative Strength Index)
- Momentum (5-day & 10-day)

---

## 🖥️ Web Application
The trained model is deployed using **Streamlit**.  
Users can enter any stock or crypto symbol and instantly get a prediction.

Example symbols:
- RELIANCE.NS
- TCS.NS
- INFY.NS
- BTC-USD
- ETH-USD

---

## 🛠 Tech Stack
- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Plotly
- Yahoo Finance API (yfinance)

---

## ▶ Run Locally

```bash
pip install -r requirements.txt

streamlit run app.py
