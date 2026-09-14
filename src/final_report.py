import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "golden_set" / "golden_set_labeled.csv"
RESULT_FILE = BASE_DIR / "results" / "evaluation_results.txt"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)
df = df.dropna(subset=["intent"])

# Same keyword classifier used in evaluation
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


df["prediction"] = df["text"].apply(classify_intent)

df["correct"] = df["intent"] == df["prediction"]

# Failure examples
failures = df[df["correct"] == False].copy()

failures = failures[
    ["tweet_id", "text", "intent", "prediction"]
]

failure_file = REPORT_DIR / "failure_candidates.csv"
failures.to_csv(failure_file, index=False)

accuracy = df["correct"].mean()

# Create report
report_file = REPORT_DIR / "evaluation_report.md"

with open(report_file, "w", encoding="utf-8") as f:

    f.write("# Hiver AI Support Agent – Evaluation Report\n\n")

    f.write("## Dataset\n\n")
    f.write(
        f"Brand selected: AppleSupport  \n"
        f"Evaluation examples: {len(df)}  \n"
        f"Evaluation method: sampled customer-support messages  \n\n"
    )

    f.write("## Results\n\n")
    f.write(f"Keyword classifier accuracy: **{accuracy:.3f}**\n\n")

    f.write("## Baselines\n\n")
    f.write(
        "- **Trivial baseline:** always predicts the most frequent intent.\n"
        "- **Simple baseline:** keyword-based intent classifier.\n"
        "- **Proposed pipeline:** intent classification + retrieval of "
        "historical AppleSupport replies + escalation decision.\n\n"
    )

    f.write("## What is misleading about my headline number?\n\n")
    f.write(
        "The headline accuracy is measured on a sampled evaluation set "
        "and the current labels were generated using an initial rule-based "
        "labeling process. Therefore, the number should not be interpreted "
        "as production-level accuracy. A manually verified golden set is "
        "required for the final evaluation.\n\n"
    )

    f.write("## Top Failure Modes\n\n")

    f.write(
        "1. Overlapping keywords can cause incorrect intent assignment.\n"
        "2. Messages with very little context are difficult to classify.\n"
        "3. Multiple issues in one customer message may belong to different intents.\n"
        "4. Generic words such as 'app' can create false matches.\n"
        "5. Unseen or unusual support issues fall into the general-support category.\n\n"
    )

    f.write("## What I would do with one more week\n\n")

    f.write(
        "1. Manually verify the 200-example golden evaluation set.\n"
        "2. Replace keyword classification with a stronger ML/LLM classifier.\n"
        "3. Improve retrieval using TF-IDF or embedding-based similarity.\n"
        "4. Add an LLM-as-judge evaluation for reply quality.\n"
        "5. Reconstruct more complete multi-turn support conversations.\n"
    )

print("===================================")
print("FINAL REPORT CREATED")
print("===================================")

print("\nAccuracy:", round(accuracy, 3))
print("Failure cases:", len(failures))

print("\nCreated:")
print(report_file)

print(failure_file)