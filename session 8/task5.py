import pandas as pd

data = {
    'title': [
        'python pandas tutorial',
        'learn data analysis',
        'excel for beginners',
        'power bi dashboard',
        'sql interview questions'
    ]
}

df = pd.DataFrame(data)

df['title'] = df['title'].str.upper()

df['title'] = df['title'].str.replace(
    ' ', '_', regex=False
)

print("Updated YouTube Titles:")
print(df)