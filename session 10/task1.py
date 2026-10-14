import pandas as pd

users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'username': ['Jaya', 'Riya', 'Aman', 'Neha', 'Rahul'],
    'city': ['Ahmedabad', 'Surat', 'Mumbai', 'Pune', 'Delhi']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107],
    'user_id': [1, 2, 1, 3, 2, 1, 3],
    'order_amount': [500, 700, 300, 900, 400, 200, 600]
})

result = pd.merge(users, orders, on='user_id', how='inner')

print("Users Who Placed Orders:")
print(result)