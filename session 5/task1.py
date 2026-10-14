import pandas as pd

df = pd.read_csv("ipl_players.csv")

missing_age = df[df["age"].isnull()]

print(missing_age)