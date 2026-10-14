import pandas as pd

data = {
    'player': ['Virat', 'Gill', 'Rohit', 'Dhoni', 'Rinku'],
    'runs': [639, 890, 332, 104, 474],
    'matches': [14, 17, 16, 16, 14],
    'average': [53.25, 59.33, 20.75, 26.00, 59.25],
    'strike_rate': [139.82, 157.80, 132.80, 182.46, 149.53]
}

df = pd.DataFrame(data)

summary = df.describe()

print("IPL Summary Statistics:")
print(summary)