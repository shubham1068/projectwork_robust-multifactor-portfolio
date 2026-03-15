import yfinance as yf
import pandas as pd
import time

tickers = [
"AAPL","MSFT","GOOGL","AMZN","NVDA","META","JPM","V","UNH","PG",
"XOM","HD","CVX","ABBV","PFE","KO","PEP","COST","TMO","AVGO"
]

prices = pd.DataFrame()

for ticker in tickers:
    try:
        print("Downloading:", ticker)

        df = yf.download(
            ticker,
            start="2020-01-01",
            auto_adjust=True,
            progress=False
        )

        if not df.empty:
            prices[ticker] = df["Close"]

        time.sleep(1)  # avoid Yahoo blocking

    except Exception as e:
        print("Failed:", ticker)

prices = prices.ffill().dropna()

prices.to_csv("stock_prices.csv")

print("Saved CSV with shape:", prices.shape)