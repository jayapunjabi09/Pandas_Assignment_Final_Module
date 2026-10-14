import pandas as pd

df = pd.read_csv("spotify_playlist.csv")

median_duration = df["duration"].median()

df["duration"] = df["duration"].fillna(median_duration)

print(df)

df.to_csv("spotify_playlist_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")