import pandas as pd

df = pd.read_csv("instagram_users.csv")

df["followers"] = df["followers"].fillna(0)

print(df)

df.to_csv("instagram_users_cleaned.csv", index=False)