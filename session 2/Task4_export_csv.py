import pandas as pd

ipl_data = pd.read_csv("ipl_matches.csv")

filtered_data = ipl_data.head(20)

filtered_data.to_csv("filtered_data.csv", index=False)

print("First 20 rows saved successfully!")