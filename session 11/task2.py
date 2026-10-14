import pandas as pd

products = pd.DataFrame({
    'product_id': [101, 102, 103],
    'product_name': ['Mobile', 'Laptop', 'Shoes'],
    'price': [15000, 45000, 2000]
})

ratings = pd.DataFrame({
    'rating': [4.5, 4.2, 4.8],
    'reviews': [200, 150, 300]
})

result = pd.concat([products, ratings], axis=1)

print("Products with Ratings:")
print(result)