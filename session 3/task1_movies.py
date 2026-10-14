import pandas as pd

movies = pd.read_csv("movies.csv")

result = movies.loc[:, ["title", "rating"]]

print(result)