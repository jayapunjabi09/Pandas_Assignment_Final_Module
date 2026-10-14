import pandas as pd

playlists = pd.DataFrame({
    'playlist_id': [101, 102, 103, 104],
    'user_id': [1, 2, 3, 4],
    'genre': ['Pop', 'Rock', 'Hip Hop', 'Jazz'],
    'city': ['Ahmedabad', 'Surat', 'Mumbai', 'Pune']
})

profiles = pd.DataFrame({
    'user_id': [1, 2, 3, 5],
    'username': ['Jaya', 'Riya', 'Aman', 'Neha'],
    'city': ['Ahmedabad', 'Surat', 'Delhi', 'Pune']
})

result = pd.merge(
    playlists,
    profiles,
    on=['user_id', 'city'],
    how='inner'
)

print("Matched Playlists and Profiles:")
print(result)