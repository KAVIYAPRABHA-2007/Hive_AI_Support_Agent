import pandas as pd
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "golden_set" / "golden_set_labeled.csv"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# Remove empty labels
df = df.dropna(subset=["intent"])

# -----------------------------
# Baseline 1: Majority Class
# -----------------------------

majority_intent = df["intent"].value_counts().idxmax()

majority_correct = sum(
    df["intent"] == majority_intent
)

majority_accuracy = majority_correct / len(df)


# -----------------------------
# Baseline 2: Keyword Classifier
# -----------------------------

def classify_intent(text):
    text = str(text).lower()

    if any(x in text for x in ["update", "ios", "software update"]):
        return "ios_update"

    if any(x in text for x in ["battery", "charging", "charger", "charge"]):
        return "battery_charging"

    if any(x in text for x in [
        "volume", "sound", "speaker",
        "headphone", "earphone"
    ]):
        return "audio_headphone"

    if "apple music" in text:
        return "apple_music"

    if any(x in text for x in [
        "activation", "apple id",
        "icloud", "password"
    ]):
        return "activation_account"

    if any(x in text for x in [
        "app", "download", "install"
    ]):
        return "apps_software"

    if any(x in text for x in [
        "slow", "freeze", "lag", "crash"
    ]):
        return "device_performance"

    return "other_general_support"


df["predicted_intent"] = df["text"].apply(classify_intent)

keyword_accuracy = (
    df["predicted_intent"] == df["intent"]
).mean()


# -----------------------------
# Per-intent results
# -----------------------------

intent_results = []

for intent in sorted(df["intent"].unique()):

    actual = df["intent"] == intent
    predicted = df["predicted_intent"] == intent

    support = actual.sum()

    correct = (actual & predicted).sum()

    accuracy = correct / support if support else 0

    intent_results.append({
        "intent": intent,
        "examples": support,
        "correct": correct,
        "accuracy": round(accuracy, 3)
    })

intent_df = pd.DataFrame(intent_results)


# -----------------------------
# Save results
# -----------------------------

results_file = RESULTS_DIR / "evaluation_results.txt"

with open(results_file, "w", encoding="utf-8") as f:

    f.write("HIVER AI SUPPORT AGENT - EVALUATION\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Evaluation examples: {len(df)}\n\n")

    f.write("BASELINE 1 - MAJORITY CLASS\n")
    f.write(f"Majority intent: {majority_intent}\n")
    f.write(f"Accuracy: {majority_accuracy:.3f}\n\n")

    f.write("BASELINE 2 - KEYWORD CLASSIFIER\n")
    f.write(f"Accuracy: {keyword_accuracy:.3f}\n\n")

    f.write("PER-INTENT RESULTS\n")
    f.write(intent_df.to_string(index=False))

print("\n==============================")
print("EVALUATION COMPLETE")
print("==============================")

print("\nTotal examples:", len(df))

print("\nBaseline 1 - Majority class")
print("Intent:", majority_intent)
print("Accuracy:", round(majority_accuracy, 3))

print("\nBaseline 2 - Keyword classifier")
print("Accuracy:", round(keyword_accuracy, 3))

print("\nPer-intent results:")
print(intent_df.to_string(index=False))

print("\nSaved:")
print(results_file)