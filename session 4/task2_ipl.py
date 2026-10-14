import pandas as pd

ipl = pd.DataFrame({
    "team": ["MI", "CSK", "RCB", "KKR", "GT", "RR"],
    "points": [14, 18, 16, 20, 12, 14],
    "net_run_rate": [0.45, 0.65, 0.32, 0.75, -0.15, 0.40]
})

result = ipl.sort_index(ascending=False)

print(result)