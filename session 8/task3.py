import pandas as pd

data = {
    'review': [
        'Fast delivery and good food',
        'Food was tasty',
        'Delivery was late',
        'Amazing restaurant',
        'DELIVERY was very quick'
    ]
}

df = pd.DataFrame(data)

result = df[
    df['review'].str.contains(
        'delivery', case=False, na=False
    )
]

print("Reviews Containing Delivery:")
print(result)