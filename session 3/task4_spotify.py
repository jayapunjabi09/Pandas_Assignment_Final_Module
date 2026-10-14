import pandas as pd

songs = pd.DataFrame({
    "song": [
        "Song A", "Song B", "Song C",
        "Song D", "Song E"
    ],
    "artist": [
        "Arijit", "Shreya", "Neha",
        "Atif", "Armaan"
    ],
    "streams": [
        1500000, 800000, 2000000,
        1200000, 500000
    ],
    "duration": [
        170, 200, 150, 190, 160
    ]
})

result = songs.query(
    "streams > 1000000 and duration < 180"
)

print(result)