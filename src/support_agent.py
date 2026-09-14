import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "applesupport_customer.csv"

df = pd.read_csv(DATA_FILE)


def classify_intent(text):
    text = text.lower()

    if any(x in text for x in ["update", "ios", "software update"]):
        return "ios_update"

    if any(x in text for x in ["battery", "charging", "charger", "charge"]):
        return "battery_charging"

    if any(x in text for x in ["volume", "sound", "speaker", "headphone", "earphone"]):
        return "audio_headphone"

    if "apple music" in text:
        return "apple_music"

    if any(x in text for x in ["activation", "apple id", "icloud", "password"]):
        return "activation_account"

    if any(x in text for x in ["app", "download", "install"]):
        return "apps_software"

    if any(x in text for x in ["slow", "freeze", "lag", "crash"]):
        return "device_performance"

    return "other_general_support"


def generate_reply(intent):
    replies = {
        "ios_update":
            "Thanks for contacting Apple Support. Please make sure your device is backed up and running the latest supported iOS version.",

        "battery_charging":
            "Thanks for reaching out. Please check the charging cable, adapter, and charging port, and try another compatible charger if available.",

        "audio_headphone":
            "Thanks for contacting Apple Support. Please check the volume settings and reconnect your headphones or audio device.",

        "apple_music":
            "Thanks for reaching out. Please check your Apple Music subscription, internet connection, and try restarting the app.",

        "activation_account":
            "Thanks for contacting Apple Support. Please verify your Apple Account credentials and follow the official account recovery or activation steps.",

        "apps_software":
            "Thanks for contacting Apple Support. Please check that your device software is up to date and try restarting the affected app.",

        "device_performance":
            "Thanks for contacting Apple Support. Please restart your device and check available storage and software updates.",

        "other_general_support":
            "Thanks for contacting Apple Support. Please share a few more details about the issue so we can help you further."
    }

    return replies[intent]


def decide_escalation(intent):
    if intent in ["activation_account", "other_general_support"]:
        return "escalate", "The issue may require account-specific or additional human investigation."

    return "auto-handle", "The issue matches a common support category with a standard troubleshooting response."


if __name__ == "__main__":
    message = input("Customer message: ")

    intent = classify_intent(message)
    reply = generate_reply(intent)
    decision, reason = decide_escalation(intent)

    print("\nIntent:", intent)
    print("Draft reply:", reply)
    print("Decision:", decision)
    print("Reason:", reason)