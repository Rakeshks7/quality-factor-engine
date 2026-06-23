# Quality Factor Engine: Smart Beta Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas)
![Statsmodels](https://img.shields.io/badge/Statsmodels-0.14%2B-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A modular, production-grade systematic equity pipeline designed to harvest the **Quality Factor** premium. This engine processes point-in-time accounting data, ranks equities using cross-sectional z-scores (high profitability / low debt), constructs a dollar-neutral Long/Short portfolio, and validates alpha using the Fama-French 5-Factor regression model.

## Features

* **Point-in-Time Data Merging:** Utilizes `pd.merge_asof` to rigorously simulate reporting lags and eliminate look-ahead bias.
* **Cross-Sectional Factor Scoring:** Normalizes raw accounting ratios (ROE, Debt-to-Equity) daily across the trading universe using z-scores.
* **Dollar-Neutral Portfolio Construction:** Automatically balances $1M Long (Top decile Quality) and $1M Short (Bottom decile Junk) positions.
* **Alpha Validation:** Built-in regression engine utilizing OLS to test strategy returns against the Fama-French 5-Factor model (Market, SMB, HML, RMW, CMA).

## 📁 Repository Structure

```text
quality_factor_engine/
│
├── requirements.txt         # Project dependencies
├── config.py                # Capital allocations, factor weights, and constants
├── data_loader.py           # Synthetic market data generation and PIT merging
├── factor_engine.py         # Cross-sectional z-score logic
├── portfolio_builder.py     # Dollar-neutral Long/Short allocation 
├── performance_analyzer.py  # Fama-French 5-Factor regression modeling
└── main.py                  # Pipeline execution and orchestration

## Disclaimer
Educational Purposes Only. This software is provided for educational and research purposes only. It is not financial advice, and the authors are not liable for any financial losses incurred from deploying these strategies in live markets. Always conduct your own rigorous backtesting with live, high-quality data before allocating real capital.