import pandas as pd

data = {
    'product': [
        'Electronics/Mobiles/Smartphones',
        'Home/Kitchen/Appliances',
        'Fashion/Men/Shirts',
        'Electronics/Laptops/HP',
        'Beauty/Skincare/Facewash'
    ]
}

df = pd.DataFrame(data)

df['category'] = df['product'].str.split('/').str[0]

print("Product Categories:")
print(df)