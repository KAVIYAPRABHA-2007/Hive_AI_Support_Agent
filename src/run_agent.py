import pandas as pd
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

KB_FILE = BASE_DIR / "data" / "support_knowledge_base.csv"

kb = pd.read_csv(KB_FILE)


def classify_intent(text):
    text = text.lower()

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


def similarity(query, text):
    query_words = set(re.findall(r"\b\w+\b", query.lower()))
    text_words = set(re.findall(r"\b\w+\b", text.lower()))

    if not query_words or not text_words:
        return 0

    return len(query_words & text_words) / len(query_words)


def retrieve_reply(query):
    scores = []

    for _, row in kb.iterrows():
        score = similarity(query, str(row["text"]))
        scores.append((score, str(row["text"])))

    scores.sort(reverse=True)

    return scores[0]


def decide(intent, score):
    if intent in ["activation_account", "other_general_support"]:
        return "ESCALATE", "Account-specific or unclear issue."

    if score < 0.15:
        return "ESCALATE", "No sufficiently similar historical support example."

    return "AUTO-HANDLE", "Similar historical support example found."


if __name__ == "__main__":

    message = input("Customer message: ")

    intent = classify_intent(message)

    score, historical_reply = retrieve_reply(message)

    decision, reason = decide(intent, score)

    print("\n==============================")
    print("HIVER AI SUPPORT AGENT")
    print("==============================")

    print("\nIntent:")
    print(intent)

    print("\nHistorical support example:")
    print(historical_reply)

    print("\nSimilarity score:")
    print(round(score, 3))

    print("\nDecision:")
    print(decision)

    print("\nReason:")
    print(reason)

    print("\nDraft reply:")
    print(historical_reply)