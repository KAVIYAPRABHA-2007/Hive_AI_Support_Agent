import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(file)

labels = [
    "device_performance",
    "apps_software",
    "device_performance",
    "other_general_support",
    "audio_headphone",
    "other_general_support",
    "ios_update",
    "other_general_support",
    "activation_account",
    "other_general_support",
    "ios_update",
    "device_performance",
    "other_general_support",
    "other_general_support",
    "other_general_support",
    "device_performance",
    "apps_software",
    "ios_update",
    "apps_software",
    "battery_charging"
]

df.loc[20:39, "intent"] = labels
df.to_csv(file, index=False)

print("SUCCESS: 21-40 labeled")
