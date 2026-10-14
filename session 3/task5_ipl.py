import pandas as pd

ipl = pd.DataFrame({
    "team1": [
        "MI", "CSK", "RCB", "KKR",
        "GT", "RR"
    ],
    "team2": [
        "CSK", "RCB", "MI", "GT",
        "RR", "KKR"
    ],
    "winner": [
        "MI", "CSK", "RCB", "KKR",
        "GT", "RR"
    ],
    "total_runs": [
        190, 175, 210, 225, 200, 160
    ]
})

result = ipl[
    (ipl["total_runs"] >= 180) &
    (ipl["total_runs"] <= 220)
]

print(result)