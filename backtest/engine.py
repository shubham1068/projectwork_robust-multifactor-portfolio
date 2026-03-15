import pandas as pd


def run_backtest(prices, weights):
    """
    Run portfolio backtest.

    Parameters
    ----------
    prices : DataFrame
        Price matrix (Date x Assets)

    weights : DataFrame
        Portfolio weights (Date x Assets)

    Returns
    -------
    portfolio_returns : Series
    equity_curve : Series
    """

    # daily returns
    returns = prices.pct_change()

    # shift weights to avoid look-ahead bias
    shifted_weights = weights.shift(1)

    # portfolio returns
    portfolio_returns = (shifted_weights * returns).sum(axis=1)

    # equity curve
    equity_curve = (1 + portfolio_returns).cumprod()

    return portfolio_returns, equity_curve