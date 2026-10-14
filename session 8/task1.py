import pandas as pd

data = {
    'username': ['JayaPunjabi', 'CoolDude', 'FoodieQueen', 'TravelGirl', 'InstaStar']
}

df = pd.DataFrame(data)

df['username'] = df['username'].str.lower()

print("Updated Usernames:")
print(df)