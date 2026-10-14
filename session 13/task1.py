import pandas as pd

data = {
    'player_name': ['Virat Kohli', 'Shubman Gill', 'Ruturaj Gaikwad',
                    'Faf du Plessis', 'David Warner', 'Rohit Sharma',
                    'MS Dhoni', 'Suryakumar Yadav', 'Yashasvi Jaiswal',
                    'Rinku Singh'],
    'runs': [639, 890, 590, 730, 516, 332, 104, 605, 625, 474],
    'matches': [14, 17, 16, 14, 14, 16, 16, 16, 14, 14],
    'average': [53.25, 59.33, 42.14, 56.15, 36.86,
                20.75, 26.00, 43.21, 48.08, 59.25],
    'strike_rate': [139.82, 157.80, 147.50, 153.68, 131.63,
                    132.80, 182.46, 181.13, 163.61, 149.53]
}

df = pd.DataFrame(data)

print("First 10 Rows:")
print(df.head(10))