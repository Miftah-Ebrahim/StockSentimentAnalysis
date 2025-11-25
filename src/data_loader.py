import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker="AAPL", period="5y"):
    df = yf.download(ticker, period=period)
    df.reset_index(inplace=True)
    return df


def load_local_news(path="data/raw/news_raw.csv"):
    return pd.read_csv(path)
