import pandas as pd

followers = pd.Series([1200, 54000, 780, 150000, 32000])

print("Highest followers:", followers.max())
print("Lowest followers:", followers.min())
print("Index of highest followers:", followers.idxmax())
print("Index of lowest followers:", followers.idxmin())