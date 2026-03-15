import pandas as pd

def compute_value(prices, window=252):
    """
    Value proxy using long-term mean reversion
    """

    ma = prices.rolling(window).mean()

    value = ma / prices

    return value