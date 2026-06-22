import pandas as pd
import numpy as np
import statsmodels.api as sm

def generate_mock_fama_french_data(index_dates):
    ff_data = pd.DataFrame(index=index_dates)
    ff_data['Mkt-RF'] = np.random.normal(0.0003, 0.01, len(index_dates))
    ff_data['SMB'] = np.random.normal(0.0001, 0.005, len(index_dates))
    ff_data['HML'] = np.random.normal(0.0001, 0.005, len(index_dates))
    ff_data['RMW'] = np.random.normal(0.0002, 0.005, len(index_dates))
    ff_data['CMA'] = np.random.normal(0.0001, 0.005, len(index_dates))
    ff_data['RF'] = 0.0001 # Daily risk free rate
    return ff_data

def run_fama_french_regression(portfolio_returns):
    ff_data = generate_mock_fama_french_data(portfolio_returns.index)

    excess_returns = portfolio_returns - ff_data['RF']

    X = ff_data[['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA']]
    X = sm.add_constant(X)
    y = excess_returns

    model = sm.OLS(y, X).fit()
    
    return model