import pandas as pd

data = {
    'user': ['Jaya', 'Jaya', 'Riya', 'Riya', 'Aman', 'Aman'],
    'day': ['Monday', 'Tuesday', 'Monday', 'Tuesday',
            'Monday', 'Tuesday'],
    'streams': [100, 150, 200, 250, 120, 180]
}

df = pd.DataFrame(data)

result = df.pivot(
    index='user',
    columns='day',
    values='streams'
)

print("Spotify Streams:")
print(result)