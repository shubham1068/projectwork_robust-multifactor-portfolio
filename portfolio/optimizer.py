import pandas as pd

def build_portfolio(score, top_quantile=0.3):

    # rank stocks cross-sectionally
    ranks = score.rank(axis=1, pct=True)

    # select top quantile
    selected = ranks >= (1 - top_quantile)

    # equal weight
    weights = selected.div(selected.sum(axis=1), axis=0)

    weights = weights.fillna(0)

    return weights