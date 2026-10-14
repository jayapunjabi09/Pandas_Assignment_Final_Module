import pandas as pd

data = {
    'Movie': ['RRR', 'Pushpa', 'KGF', 'Jawan'],
    'release_date': [
        '2022-03-25',
        '2021-12-17',
        '2022-04-14',
        '2023-09-07'
    ]
}

df = pd.DataFrame(data)

df['release_date'] = pd.to_datetime(df['release_date'])

df['year'] = df['release_date'].dt.year
df['month'] = df['release_date'].dt.month
df['day'] = df['release_date'].dt.day

print("Movie Release Dates:")
print(df)