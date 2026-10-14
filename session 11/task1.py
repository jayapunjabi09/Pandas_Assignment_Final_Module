import pandas as pd

january = pd.DataFrame({
    'order_id': [101, 102, 103],
    'item': ['Pizza', 'Burger', 'Pasta'],
    'amount': [200, 150, 250]
})

february = pd.DataFrame({
    'order_id': [104, 105, 106],
    'item': ['Sandwich', 'Fries', 'Pizza'],
    'amount': [100, 120, 300]
})

result = pd.concat([january, february], ignore_index=True)

print("Combined Orders:")
print(result)