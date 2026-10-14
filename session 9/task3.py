import pandas as pd

today = pd.Timestamp.today().normalize()

dates = pd.date_range(
    start=today,
    periods=8,
    freq='D'
)

dates = dates[1:]

print("Next 7 Days:")

for date in dates:
    print(date.strftime('%d-%m-%Y'))