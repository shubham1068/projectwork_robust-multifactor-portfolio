import pandas as pd

def compute_quality(prices):

    ma50 = prices.rolling(50).mean()
    ma200 = prices.rolling(200).mean()

    quality = ma50 / ma200

    return quality