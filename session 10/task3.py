import pandas as pd

restaurants = pd.DataFrame({
    'restaurant_id': [1, 2, 3, 4],
    'name': ['Dominos', 'KFC', 'Pizza Hut', 'Subway'],
    'city': ['Ahmedabad', 'Surat', 'Mumbai', 'Pune']
})

reviews = pd.DataFrame({
    'review_id': [101, 102, 103, 104],
    'restaurant_id': [1, 2, 5, 1],
    'rating': [5, 4, 3, 5],
    'reviewer_city': ['Ahmedabad', 'Surat', 'Delhi', 'Rajkot']
})

result = pd.merge(
    restaurants,
    reviews,
    on='restaurant_id',
    how='outer'
)

print("All Restaurants and Reviews:")
print(result)