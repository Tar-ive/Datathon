import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def filter_data(df, start_date, end_date, selected_states):
    return df[
        (df['Date'].dt.date >= start_date) &
        (df['Date'].dt.date <= end_date) &
        (df['State/Province'].isin(selected_states))
    ]

def get_top_towns(df, n=10):
    return df['Town'].value_counts().nlargest(n)
