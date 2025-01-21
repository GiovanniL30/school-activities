import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv')

def compute_stats(series):
    return {
        'Mean': series.mean(),
        'Median': series.median(),
        'Mode': series.mode()[0],
        'Variance': series.var(),
        'Standard Deviation': series.std(),
        'Coefficient of Variation': series.std() / series.mean(),
        'Q1': series.quantile(0.25),
        'Q3': series.quantile(0.75),
        '5th Percentile': series.quantile(0.05),
        '95th Percentile': series.quantile(0.95)
    }


microsoft_stats = compute_stats(data['Stock Price Microsoft'])
google_stats = compute_stats(data['Stock Price Google'])


microsoft_df = pd.DataFrame.from_dict(microsoft_stats, orient='index', columns=['Value'])
google_df = pd.DataFrame.from_dict(google_stats, orient='index', columns=['Value'])

print('Microsoft')
print(microsoft_df)

print('Google')
print(google_df)