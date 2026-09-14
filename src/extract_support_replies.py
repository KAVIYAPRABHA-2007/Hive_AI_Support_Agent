import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "twcs.csv")

support = df[
    (df["inbound"] == False) &
    (df["author_id"] == "AppleSupport")
][["tweet_id", "text", "in_response_to_tweet_id"]]

output_file = BASE_DIR / "data" / "applesupport_replies.csv"

support.to_csv(output_file, index=False)

print("AppleSupport replies:", len(support))
print("Saved to:", output_file)