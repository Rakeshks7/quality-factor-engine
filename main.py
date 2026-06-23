from data_loader import generate_synthetic_market_data, merge_point_in_time
from factor_engine import calculate_quality_factor
from portfolio_builder import construct_dollar_neutral_portfolio, calculate_portfolio_returns
from performance_analyzer import run_fama_french_regression

def run_pipeline():
    print("1. Ingesting Market & Accounting Data...")
    tickers = ['AAPL', 'MSFT', 'TSLA', 'JNJ', 'JPM', 'V', 'PG', 'XOM', 'META', 'UNH']
    df_prices, df_fundamentals = generate_synthetic_market_data(tickers, '2023-01-01', '2024-01-01')
    
    print("2. Performing Point-in-Time Merge...")
    df_pit = merge_point_in_time(df_prices, df_fundamentals)
    
    print("3. Computing Factor Z-Scores (Quality)...")
    df_factors = calculate_quality_factor(df_pit)
    
    print("4. Constructing Long/Short Portfolio...")
    df_portfolio = construct_dollar_neutral_portfolio(df_factors, top_percentile=0.3, bottom_percentile=0.3)
    
    print("5. Calculating Daily Strategy Returns...")
    daily_returns = calculate_portfolio_returns(df_portfolio)
    
    print("6. Running Fama-French 5-Factor Regression...\n")
    ff_model = run_fama_french_regression(daily_returns)
    
    print("-" * 60)
    print("FAMA-FRENCH REGRESSION RESULTS")
    print("-" * 60)
    print(ff_model.summary())

if __name__ == "__main__":
    run_pipeline()