import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(file)

labels = [
    "device_performance",      # 151
    "other_general_support",   # 152
    "apps_software",           # 153
    "other_general_support",   # 154
    "other_general_support",   # 155
    "device_performance",      # 156
    "device_performance",      # 157
    "device_performance",      # 158
    "battery_charging",        # 159
    "apps_software",           # 160
    "other_general_support",   # 161
    "activation_account",      # 162
    "battery_charging",        # 163
    "other_general_support",   # 164
    "other_general_support",   # 165
    "audio_headphone",         # 166
    "other_general_support",   # 167
    "ios_update",              # 168
    "ios_update",              # 169
    "device_performance",      # 170
    "device_performance",      # 171
    "device_performance",      # 172
    "device_performance",      # 173
    "other_general_support",   # 174
    "ios_update",              # 175
    "device_performance",      # 176
    "activation_account",      # 177
    "device_performance",      # 178
    "activation_account",      # 179
    "ios_update",              # 180
    "device_performance",      # 181
    "ios_update",              # 182
    "ios_update",              # 183
    "ios_update",              # 184
    "battery_charging",        # 185
    "apps_software",           # 186
    "battery_charging",        # 187
    "activation_account",      # 188
    "ios_update",              # 189
    "device_performance",      # 190
    "other_general_support",   # 191
    "apps_software",           # 192
    "apps_software",           # 193
    "other_general_support",   # 194
    "device_performance",      # 195
    "ios_update",              # 196
    "battery_charging",        # 197
    "apps_software",           # 198
    "device_performance",      # 199
    "apps_software"            # 200
]

df.loc[150:199, "intent"] = labels

df.to_csv(file, index=False)

print("================================")
print("SUCCESS: 151-200 LABELED")
print("================================")
print("Total labeled:", df["intent"].notna().sum())
print("Saved to:", file)
