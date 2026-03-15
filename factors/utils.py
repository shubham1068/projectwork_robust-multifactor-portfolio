import pandas as pd

def zscore(df):

    mean = df.mean(axis=1)
    std = df.std(axis=1)

    z = df.sub(mean, axis=0).div(std, axis=0)

    return z