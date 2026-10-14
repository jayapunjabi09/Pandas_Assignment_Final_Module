import pandas as pd

food_orders = pd.DataFrame({
    "Item": ["Pizza", "Paneer Tikka", "Burger"],
    "Restaurant": ["Dominos", "Honest", "McDonald's"],
    "Price": [250, 180, 150]
})

print(food_orders)