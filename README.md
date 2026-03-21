🚀 **Built a Robust Multi-Factor Portfolio Strategy (Quant Research Project)**


# Robust Multi-Factor Portfolio Strategy

This project implements a quantitative research pipeline for building and backtesting a robust multi-factor equity portfolio.

The strategy combines several well-known equity factors to construct a diversified portfolio with strong risk-adjusted returns.

---

## Factors Used

The model uses four core factors widely studied in quantitative finance:

- **Momentum** – Stocks with strong past returns tend to continue performing well.
- **Value** – Undervalued stocks tend to outperform over time.
- **Quality** – Companies with strong financial stability and profitability.
- **Low Volatility** – Stocks with lower volatility often deliver better risk-adjusted returns.

These factors are combined into a composite signal used to rank stocks.

---

## Research Pipeline

The project implements a full quantitative research workflow:

Price Data
↓
Factor Engineering
↓
Factor Normalization (Z-score)
↓
Composite Alpha Signal
↓
Portfolio Construction
↓
Backtesting Engine
↓
Performance Metrics 


---

## Portfolio Construction

- Cross-sectional ranking of factor scores
- Selection of top quantile stocks
- Equal-weight portfolio allocation
- Rebalanced periodically

---

## Performance Results

Example backtest results:

| Metric | Value |
|------|------|
| Sharpe Ratio | 1.12 |
| Annual Return | 22.9% |
| Volatility | 18.4% |
| Max Drawdown | -27.8% |

---

## Project Structure
project_work/

data/
prices.csv

factors/
momentum.py
value.py
quality.py
lowvol.py
utils.py

portfolio/
optimizer.py

backtest/
engine.py

metrics/
performance.py

run_strategy.py 

---

## Future Improvements

Planned improvements to the research framework:

- Transaction cost modeling
- Factor Information Coefficient (IC) analysis
- Turnover control
- Volatility targeting
- Machine learning alpha models

---

## Author

Shubham Pandey  
BSc Computational Physics – MIT World Peace University

#quantfinance #algorithmictrading #systematictrading #machinelearning #finance #portfoliooptimization #python
