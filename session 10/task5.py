import pandas as pd

products = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'name': ['Mobile', 'Laptop', 'Shoes', 'Watch'],
    'category': ['Electronics', 'Electronics', 'Fashion', 'Accessories']
})

ratings = pd.DataFrame({
    'rating_id': [1, 2, 3, 4],
    'product_id': [101, 102, 105, 103],
    'rating': [5, 4, 3, 5]
})

result = pd.merge(
    products,
    ratings,
    on='product_id',
    how='right'
)

print("Products with Ratings:")
print(result)