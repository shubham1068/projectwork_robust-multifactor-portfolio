import pandas as pd

from factors.momentum import compute_momentum
from factors.value import compute_value
from factors.lowvol import compute_lowvol
from factors.quality import compute_quality
from factors.utils import zscore

from portfolio.optimizer import build_portfolio
from backtest.engine import run_backtest


# Load data
prices = pd.read_csv("prices.csv", index_col="Date", parse_dates=True)


# Factors
momentum = zscore(compute_momentum(prices))
value = zscore(compute_value(prices))
lowvol = zscore(compute_lowvol(prices))
quality = zscore(compute_quality(prices))


# Factor score
score = (
      0.30 * momentum
    + 0.30 * value
    + 0.20 * quality
    + 0.20 * lowvol
)


# Portfolio weights
weights = build_portfolio(score)


# Run backtest
portfolio_returns, equity_curve = run_backtest(prices, weights)


print(equity_curve.tail())


from metrics.performance import (
    sharpe_ratio,
    annual_return,
    annual_volatility,
    max_drawdown
)

print("Sharpe:", sharpe_ratio(portfolio_returns))
print("Annual Return:", annual_return(portfolio_returns))
print("Volatility:", annual_volatility(portfolio_returns))
print("Max Drawdown:", max_drawdown(equity_curve))