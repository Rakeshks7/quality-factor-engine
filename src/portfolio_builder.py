import pandas as pd
import config

def construct_dollar_neutral_portfolio(df_factors, top_percentile=0.2, bottom_percentile=0.2):
    portfolio_returns = []

    for date, daily_data in df_factors.groupby('date'):
        upper_threshold = daily_data['quality_score'].quantile(1 - top_percentile)
        lower_threshold = daily_data['quality_score'].quantile(bottom_percentile)

        longs = daily_data[daily_data['quality_score'] >= upper_threshold].copy()
        shorts = daily_data[daily_data['quality_score'] <= lower_threshold].copy()

        long_weight = config.LONG_EXPOSURE / len(longs) if not longs.empty else 0
        short_weight = config.SHORT_EXPOSURE / len(shorts) if not shorts.empty else 0

        longs['target_weight'] = long_weight
        shorts['target_weight'] = short_weight
        
        daily_portfolio = pd.concat([longs, shorts])
        portfolio_returns.append(daily_portfolio)
        
    return pd.concat(portfolio_returns)

def calculate_portfolio_returns(df_portfolio):
    df_portfolio['next_day_price'] = df_portfolio.groupby('ticker')['close'].shift(-1)
    df_portfolio['daily_return'] = (df_portfolio['next_day_price'] / df_portfolio['close']) - 1

    df_portfolio['pnl'] = df_portfolio['target_weight'] * df_portfolio['daily_return']

    daily_strategy_return = df_portfolio.groupby('date')['pnl'].sum() / config.INITIAL_CAPITAL
    return daily_strategy_return.dropna()