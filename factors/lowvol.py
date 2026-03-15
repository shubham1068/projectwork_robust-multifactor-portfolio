import pandas as pd

def compute_lowvol(prices, window=126):
    """
    Low volatility factor
    """

    returns = prices.pct_change()

    vol = returns.rolling(window).std()

    lowvol = -vol

    return lowvol