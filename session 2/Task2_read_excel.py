import pandas as pd

expenses = pd.read_excel("mobile_expenses.xlsx")

print(expenses.tail(3))