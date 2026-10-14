import pandas as pd

jan = pd.DataFrame({
    'product': ['Jeans', 'Tshirt', 'Shoes'],
    'sales': [5000, 3000, 7000]
})

feb = pd.DataFrame({
    'product': ['Jeans', 'Tshirt', 'Shoes'],
    'sales': [6000, 4000, 8000]
})

jan.to_csv('sales_jan.csv', index=False)
feb.to_csv('sales_feb.csv', index=False)

df1 = pd.read_csv('sales_jan.csv')
df2 = pd.read_csv('sales_feb.csv')

combined = pd.concat([df1, df2], ignore_index=True)

result = combined.groupby('product')['sales'].sum()

print("Combined Monthly Sales:")
print(combined)

print("\nTotal Sales by Product:")
print(result)