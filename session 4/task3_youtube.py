import pandas as pd

videos = pd.DataFrame({
    "video_title": [
        "Python Tutorial", "Music Video",
        "Travel Vlog", "Cooking Recipe"
    ],
    "views": [150000, 500000, 80000, 120000],
    "likes": [10000, 40000, 5000, 8000]
}, index=[10, 20, 30, 40])

print("Before resetting index:")
print(videos)

result = videos.reset_index(drop=True)

print("\nAfter resetting index:")
print(result)