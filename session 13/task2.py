import pandas as pd

data = {
    'player_name': ['Virat', 'Gill', 'Rohit', 'Dhoni', 'Rinku'],
    'runs': [639, 890, 332, 104, 474]
}

df = pd.DataFrame(data)

print("Mean:", df['runs'].mean())

print("Median:", df['runs'].median())

print("Mode:", df['runs'].mode().tolist())

print("Minimum:", df['runs'].min())

print("Maximum:", df['runs'].max())