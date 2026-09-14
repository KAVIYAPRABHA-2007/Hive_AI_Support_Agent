import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(file)

labels = [
    "device_performance",
    "other_general_support",
    "ios_update",
    "ios_update",
    "device_performance",
    "device_performance",
    "activation_account",
    "ios_update",
    "apps_software",
    "ios_update",
    "audio_headphone",
    "device_performance",
    "apps_software",
    "ios_update",
    "other_general_support",
    "activation_account",
    "ios_update",
    "other_general_support",
    "device_performance",
    "other_general_support"
]

df.loc[60:79, "intent"] = labels
df.to_csv(file, index=False)

print("SUCCESS: 61-80 labeled")
