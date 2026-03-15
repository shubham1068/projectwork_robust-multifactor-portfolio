import pandas as pd

from factors.momentum import compute_momentum
from factors.value import compute_value
from factors.lowvol import compute_lowvol
from factors.quality import compute_quality
from factors.utils import zscore

prices = pd.read_csv("prices.csv", index_col="Date", parse_dates=True)

momentum = zscore(compute_momentum(prices))
value = zscore(compute_value(prices))
lowvol = zscore(compute_lowvol(prices))
quality = zscore(compute_quality(prices))

score = (
      0.30 * momentum
    + 0.30 * value
    + 0.20 * quality
    + 0.20 * lowvol
)

print(score.tail())