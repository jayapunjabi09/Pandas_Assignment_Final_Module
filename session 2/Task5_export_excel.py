import pandas as pd

restaurants = pd.read_excel("restaurant_data.xlsx")

restaurants.to_excel("restaurant_analysis.xlsx", sheet_name="Analysis2024", index=False)

print("Excel file saved successfully!")