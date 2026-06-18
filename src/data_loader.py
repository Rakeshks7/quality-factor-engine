import pandas as pd
import numpy as np

def generate_synthetic_market_data(tickers, start_date, end_date):
    dates = pd.date_range(start_date, end_date, freq='B')

    price_records = []
    for ticker in tickers:
        prices = np.cumprod(1 + np.random.normal(0.0005, 0.02, len(dates))) * 100
        for i, date in enumerate(dates):
            price_records.append({'date': date, 'ticker': ticker, 'close': prices[i]})
    
    df_prices = pd.DataFrame(price_records).sort_values(['ticker', 'date'])

    accounting_records = []
    quarter_ends = pd.date_range(start_date, end_date, freq='Q')
    for ticker in tickers:
        for q_end in quarter_ends:
            release_date = q_end + pd.Timedelta(days=45) 
            accounting_records.append({
                'release_date': release_date,
                'ticker': ticker,
                'net_income': np.random.uniform(10, 100),
                'total_equity': np.random.uniform(100, 500),
                'total_debt': np.random.uniform(20, 300)
            })
            
    df_fundamentals = pd.DataFrame(accounting_records).sort_values(['ticker', 'release_date'])
    
    return df_prices, df_fundamentals

def merge_point_in_time(df_prices, df_fundamentals):
    df_prices = df_prices.sort_values('date')
    df_fundamentals = df_fundamentals.sort_values('release_date')

    merged_data = []
    for ticker in df_prices['ticker'].unique():
        p_ticker = df_prices[df_prices['ticker'] == ticker]
        f_ticker = df_fundamentals[df_fundamentals['ticker'] == ticker]

        merged = pd.merge_asof(
            p_ticker, 
            f_ticker, 
            left_on='date', 
            right_on='release_date', 
            direction='backward' 
        )
        merged_data.append(merged)
        
    df_final = pd.concat(merged_data).dropna()
    return df_final