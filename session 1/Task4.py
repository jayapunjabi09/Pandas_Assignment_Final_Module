import pandas as pd

playlist = pd.DataFrame({
    "Song": ["Kesariya", "Apna Bana Le", "Tum Hi Ho", "Chaleya"],
    "Artist": ["Arijit Singh", "Arijit Singh", "Arijit Singh", "Arijit Singh"],
    "Duration": [4.28, 4.21, 4.22, 3.20]
})

print(playlist[["Song", "Duration"]])