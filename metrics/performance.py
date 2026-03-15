import numpy as np


def sharpe_ratio(returns):
    return np.sqrt(252) * returns.mean() / returns.std()


def annual_return(returns):
    return (1 + returns.mean()) ** 252 - 1


def annual_volatility(returns):
    return returns.std() * np.sqrt(252)


def max_drawdown(equity):

    peak = equity.cummax()
    drawdown = (equity - peak) / peak

    return drawdown.min()