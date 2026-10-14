import pandas as pd

data = {
    'user_id': [101, 102, 103, 104],
    'start_date': [
        '2025-01-10',
        '2025-06-15',
        '2026-01-20',
        '2026-05-05'
    ]
}

df = pd.DataFrame(data)

df['start_date'] = pd.to_datetime(df['start_date'])

today = pd.Timestamp.today().normalize()

df['tenure_days'] = (today - df['start_date']).dt.days

print("Zomato Gold Subscription Tenure:")
print(df)