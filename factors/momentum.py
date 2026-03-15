import pandas as pd

def compute_momentum(prices, lookback=252, skip=21):
    """
    Momentum = past 12 month return excluding last month
    """

    momentum = prices.pct_change(lookback)
    momentum = momentum.shift(skip)

    return momentum