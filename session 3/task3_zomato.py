import pandas as pd

orders = pd.DataFrame({
    "restaurant": [
        "Dominos", "Pizza Hut", "KFC",
        "McDonalds", "Honest", "Subway"
    ],
    "order_amount": [
        650, 450, 800, 300, 700, 550
    ],
    "delivery_time": [
        30, 25, 40, 20, 35, 28
    ]
})

result = orders[orders["order_amount"] > 500]

print(result)