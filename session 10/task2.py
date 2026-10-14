import pandas as pd

users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'username': ['Jaya', 'Riya', 'Aman', 'Neha', 'Rahul']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103],
    'user_id': [1, 2, 3],
    'order_amount': [500, 700, 900]
})

result = pd.merge(users, orders, on='user_id', how='left')

print("All Users with Orders:")
print(result)