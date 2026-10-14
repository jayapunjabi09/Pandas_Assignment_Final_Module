import pandas as pd

dates = pd.Series([
    '12-10-2026',
    '15-08-2025',
    '20-01-2024',
    '05-06-2023',
    '25-12-2022'
])

result = pd.to_datetime(dates, format='%d-%m-%Y')

print("Converted Dates:")
print(result)