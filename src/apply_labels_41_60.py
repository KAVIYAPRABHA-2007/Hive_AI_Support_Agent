import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(file)

labels = [
    "apps_software",
    "ios_update",
    "other_general_support",
    "apple_music",
    "activation_account",
    "apple_music",
    "device_performance",
    "device_performance",
    "apple_music",
    "apps_software",
    "other_general_support",
    "device_performance",
    "other_general_support",
    "activation_account",
    "apple_music",
    "ios_update",
    "device_performance",
    "activation_account",
    "other_general_support",
    "ios_update"
]

df.loc[40:59, "intent"] = labels
df.to_csv(file, index=False)

print("SUCCESS: 41-60 labeled")
