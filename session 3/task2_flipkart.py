import pandas as pd

products = pd.DataFrame({
    "product_name": [
        "iPhone", "Laptop", "Headphones",
        "Shoes", "Watch", "Bag",
        "T-shirt", "Jeans", "Speaker",
        "Keyboard", "Mouse", "Tablet"
    ],
    "category": [
        "Electronics", "Electronics", "Electronics",
        "Fashion", "Accessories", "Fashion",
        "Fashion", "Fashion", "Electronics",
        "Electronics", "Electronics", "Electronics"
    ],
    "price": [
        80000, 50000, 1500,
        2000, 3000, 1200,
        500, 1500, 2500,
        800, 600, 20000
    ]
})

print(products.iloc[:10, :])