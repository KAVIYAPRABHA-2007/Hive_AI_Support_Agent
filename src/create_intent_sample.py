import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "applesupport_customer.csv")

sample = df[["tweet_id", "text"]].sample(
    n=200,
    random_state=42
)

output_file = BASE_DIR / "golden_set" / "labeling_sample.csv"

sample.to_csv(output_file, index=False)

print("Created:", len(sample), "messages")
print("Saved to:", output_file)