import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(file)

labels = [
    "device_performance",
    "other_general_support",
    "apps_software",
    "other_general_support",
    "other_general_support",
    "ios_update",
    "device_performance",
    "device_performance",
    "battery_charging",
    "apps_software",
    "other_general_support",
    "activation_account",
    "battery_charging",
    "other_general_support",
    "audio_headphone",
    "other_general_support",
    "ios_update",
    "ios_update",
    "device_performance",
    "device_performance",
    "device_performance",
    "device_performance",
    "other_general_support",
    "ios_update",
    "device_performance",
    "activation_account",
    "device_performance",
    "activation_account",
    "ios_update",
    "device_performance",
    "ios_update",
    "ios_update",
    "ios_update",
    "battery_charging",
    "apps_software",
    "battery_charging",
    "activation_account",
    "ios_update",
    "device_performance",
    "other_general_support",
    "apps_software",
    "apps_software",
    "other_general_support",
    "device_performance",
    "ios_update",
    "battery_charging",
    "apps_software",
    "device_performance",
    "device_performance",
    "apps_software"
]

df.loc[100:149, "intent"] = labels
df.to_csv(file, index=False)

print("SUCCESS: 101-150 labeled")
