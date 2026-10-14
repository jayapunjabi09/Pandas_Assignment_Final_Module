import pandas as pd

products = pd.DataFrame({
    "product_name": [
        "Laptop", "Mobile", "Headphones",
        "Shoes", "Watch", "Bag"
    ],
    "price": [50000, 30000, 2000, 1500, 3000, 1200],
    "discount": [10, 20, 40, 30, 15, 25]
})

sorted_products = products.sort_values(
    by="discount",
    ascending=False
)

result = sorted_products.reset_index(drop=True)

print(result)