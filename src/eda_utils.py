import pandas as pd
import talib


def add_technical_indicators(df):
    """
    Computes technical indicators (SMA, RSI, MACD) for a given stock dataframe.

    Args:
        df (pd.DataFrame): Dataframe containing 'close' and 'date' columns.

    Returns:
        pd.DataFrame: The original dataframe with new indicator columns added.
    """
    # Safety Check: Ensure data is sorted by date or math will be wrong
    df = df.sort_values("date")

    # --- 1. Moving Averages (Trend) ---
    # SMA 20: Short-term trend
    df["SMA_20"] = talib.SMA(df["close"], timeperiod=20)

    # SMA 50: Medium-term trend
    df["SMA_50"] = talib.SMA(df["close"], timeperiod=50)

    # --- 2. RSI (Momentum) ---
    # RSI > 70 = Overbought, RSI < 30 = Oversold
    df["RSI"] = talib.RSI(df["close"], timeperiod=14)

    # --- 3. MACD (Trend Reversal) ---
    # MACD Line, Signal Line, Histogram
    macd, signal, hist = talib.MACD(
        df["close"], fastperiod=12, slowperiod=26, signalperiod=9
    )
    df["MACD"] = macd
    df["MACD_Signal"] = signal

    return df
