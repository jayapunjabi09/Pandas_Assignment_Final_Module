import pandas as pd

data = {
    'song': ['Perfect Remix', 'Believer', 'Faded Remix',
             'Shape of You Remix', 'Alone']
}

df = pd.DataFrame(data)

df['song'] = df['song'].str.replace(
    'Remix', '', case=False, regex=False
).str.strip()

print("Cleaned Song Titles:")
print(df)