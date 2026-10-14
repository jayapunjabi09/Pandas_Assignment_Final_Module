import pandas as pd

df = pd.read_csv("product_reviews.csv")

mean_rating = df["rating"].mean()

df["rating"] = df["rating"].fillna(mean_rating)

print(df)