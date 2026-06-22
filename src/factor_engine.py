import pandas as pd
from scipy.stats import zscore

def calculate_quality_factor(df):
    df['roe'] = df['net_income'] / df['total_equity']
    df['debt_to_equity'] = df['total_debt'] / df['total_equity']

    def cross_sectional_zscore(group):
        group['z_roe'] = zscore(group['roe'], nan_policy='omit')
        group['z_debt'] = zscore(group['debt_to_equity'], nan_policy='omit')
        return group
        
    df = df.groupby('date', group_keys=False).apply(cross_sectional_zscore)

    df['quality_score'] = (df['z_roe'] * 0.5) - (df['z_debt'] * 0.5)
    
    return df