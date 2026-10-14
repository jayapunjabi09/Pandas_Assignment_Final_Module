import pandas as pd

data = {
    'name': ['Dominos', 'KFC', 'Pizza Hut', 'Subway', 'Burger King'],
    'rating': [4.5, 4.2, 4.0, 3.8, 4.6],
    'votes': [500, 400, 350, 250, 600],
    'avg_cost': [500, 600, 700, 400, 550]
}

df = pd.DataFrame(data)

correlation = df['rating'].corr(df['votes'])

print("Zomato Restaurant Data:")
print(df)

print("\nCorrelation Between Rating and Votes:")
print(correlation)