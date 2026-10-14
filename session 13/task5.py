import pandas as pd

data = {
    'player': ['Virat', 'Gill', 'Rohit', 'Dhoni', 'Rinku'],
    'runs': [639, 890, 332, 104, 474],
    'strike_rate': [139.82, 157.80, 132.80, 182.46, 149.53]
}

df = pd.DataFrame(data)

# Analysis 1: Top 3 run scorers
top_players = df.sort_values(
    by='runs', ascending=False
).head(3)

print("Top 3 Run Scorers:")
print(top_players)

# Analysis 2: Players with strike rate above 150
high_strike_rate = df[df['strike_rate'] > 150]

print("\nPlayers with Strike Rate Above 150:")
print(high_strike_rate)