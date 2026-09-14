import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(file)

labels = [
    "device_performance",
    "other_general_support",
    "other_general_support",
    "other_general_support",
    "other_general_support",
    "device_performance",
    "other_general_support",
    "other_general_support",
    "apps_software",
    "other_general_support",
    "other_general_support",
    "device_performance",
    "other_general_support",
    "ios_update",
    "activation_account",
    "device_performance",
    "battery_charging",
    "apple_music",
    "device_performance",
    "activation_account"
]

df.loc[80:99, "intent"] = labels
df.to_csv(file, index=False)

print("SUCCESS: 81-100 labeled")
