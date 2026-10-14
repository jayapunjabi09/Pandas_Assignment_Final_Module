import pandas as pd

movies = pd.DataFrame({
    "title": [
        "3 Idiots", "Dangal", "PK",
        "Jawan", "12th Fail", "Pathaan"
    ],
    "rating": [8.4, 8.3, 8.1, 7.0, 8.8, 5.9],
    "release_year": [2009, 2016, 2014, 2023, 2023, 2023]
})

result = movies.sort_values(by="rating", ascending=False)

print(result)