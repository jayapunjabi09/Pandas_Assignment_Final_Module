import pandas as pd

df = pd.read_csv("food_delivery.csv")

cleaned_df = df.dropna(subset=["delivery_rating"])

print(cleaned_df)