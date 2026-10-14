import pandas as pd

restaurants = pd.read_excel("restaurant_data.xlsx")

print("Restaurant Data Information:")
restaurants.info()

print("\nStatistical Summary:")
print(restaurants.describe())