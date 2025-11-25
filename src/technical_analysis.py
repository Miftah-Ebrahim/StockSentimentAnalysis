import pandas as pd
import talib


def add_technical_indicators(df):
    """
    Computes technical indicators (SMA, RSI, MACD) for a given stock dataframe.

    This function expects a dataframe representing a SINGLE stock.
    It sorts the data by date to ensure accurate calculations.

    Args:
        df (pd.DataFrame): Dataframe containing 'close' and 'date' columns.

    Returns:
        pd.DataFrame: The original dataframe with new indicator columns added.
    """

    # 1. Sort by Date
    # Technical analysis requires chronological order.
    # If the data is scrambled, the moving averages will be wrong.
    df = df.sort_values("date")

    # 2. Moving Averages (The Trend)
    # SMA 20: Short-term trend (approx 1 month)
    df["SMA_20"] = talib.SMA(df["close"], timeperiod=20)

    # SMA 50: Medium-term trend (approx 1 quarter)
    df["SMA_50"] = talib.SMA(df["close"], timeperiod=50)

    # 3. RSI (The Momentum)
    # Relative Strength Index (0-100).
    # > 70 usually means Overbought (Price might drop).
    # < 30 usually means Oversold (Price might rise).
    df["RSI"] = talib.RSI(df["close"], timeperiod=14)

    # 4. MACD (The Signal)
    # Moving Average Convergence Divergence.
    # Used to spot changes in the strength, direction, momentum, and duration of a trend.
    macd, macd_signal, macd_hist = talib.MACD(
        df["close"], fastperiod=12, slowperiod=26, signalperiod=9
    )

    df["MACD"] = macd
    df["MACD_Signal"] = macd_signal

    return df
