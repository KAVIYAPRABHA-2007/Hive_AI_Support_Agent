import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "golden_set" / "golden_set.csv"
output_file = BASE_DIR / "golden_set" / "golden_set_labeled.csv"

df = pd.read_csv(input_file)

def assign_intent(text):
    text = str(text).lower()

    if any(word in text for word in ["update", "ios", "software update"]):
        return "ios_update"
    elif any(word in text for word in ["battery", "charging", "charger", "charge"]):
        return "battery_charging"
    elif any(word in text for word in ["volume", "sound", "speaker", "headphone", "earphone"]):
        return "audio_headphone"
    elif any(word in text for word in ["apple music", "music"]):
        return "apple_music"
    elif any(word in text for word in ["activation", "apple id", "icloud", "password"]):
        return "activation_account"
    elif any(word in text for word in ["app", "download", "install"]):
        return "apps_software"
    elif any(word in text for word in ["slow", "freeze", "lag", "crash"]):
        return "device_performance"
    else:
        return "other_general_support"

df["intent"] = df["text"].apply(assign_intent)

df.to_csv(output_file, index=False)

print("Labeled:", len(df), "messages")
print("Saved to:", output_file)
print("\nIntent counts:")
print(df["intent"].value_counts())
