import pandas as pd

data = {
    'restaurant': ['KFC', 'KFC', 'Dominos', 'Dominos',
                   'Pizza Hut', 'Pizza Hut'],
    'month': ['January', 'February', 'January',
              'February', 'January', 'February'],
    'total_amount': [500, 700, 400, 600, 800, 1000]
}

df = pd.DataFrame(data)

result = df.pivot_table(
    index='restaurant',
    columns='month',
    values='total_amount',
    aggfunc='mean'
)

print("Average Order Amount:")
print(result)