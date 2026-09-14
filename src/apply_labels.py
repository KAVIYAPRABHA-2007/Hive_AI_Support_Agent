import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "golden_set" / "labeling_sample.csv"
output_file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(input_file)

labels = [
    "activation_account",
    "device_performance",
    "apps_software",
    "audio_headphone",
    "ios_update",
    "ios_update",
    "apps_software",
    "device_performance",
    "device_performance",
    "ios_update",
    "other_general_support",
    "ios_update",
    "apps_software",
    "device_performance",
    "device_performance",
    "other_general_support",
    "activation_account",
    "apps_software",
    "device_performance",
    "other_general_support"
]

df["intent"] = ""

df.loc[:19, "intent"] = labels

df.to_csv(output_file, index=False)

print("SUCCESS")
print("First 20 messages labeled.")
print("Saved to:", output_file)
print(df.head(20).to_string(index=False))
