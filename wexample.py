import pandas as pd

from factors.momentum import compute_momentum
from factors.value import compute_value
from factors.lowvol import compute_lowvol
from factors.quality import compute_quality
from factors.utils import zscore

from portfolio.optimizer import build_portfolio




# 1️⃣ Load price data
prices =prices = pd.read_csv("prices.csv", index_col="Date", parse_dates=True)


# 2️⃣ Compute returns
returns = prices.pct_change()


# 3️⃣ Compute factors
momentum = zscore(compute_momentum(prices))
value = zscore(compute_value(prices))
lowvol = zscore(compute_lowvol(prices))
quality = zscore(compute_quality(prices))


# 4️⃣ Combine factors
score = (
      0.30 * momentum
    + 0.30 * value
    + 0.20 * quality
    + 0.20 * lowvol
)


# 5️⃣ Build portfolio
weights = build_portfolio(score)


# 6️⃣ Portfolio returns
portfolio_returns = (weights.shift(1) * returns).sum(axis=1)


# 7️⃣ Equity curve
equity_curve = (1 + portfolio_returns).cumprod()


print(equity_curve.tail())