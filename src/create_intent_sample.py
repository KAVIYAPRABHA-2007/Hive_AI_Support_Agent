import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "applesupport_customer.csv"
output_file = BASE_DIR / "golden_set" / "labeling_sample.csv"

df = pd.read_csv(input_file)

sample = df[["tweet_id", "text"]].sample(n=200, random_state=42)

sample.to_csv(output_file, index=False)

print("SUCCESS")
print("Rows:", len(sample))
print("File:", output_file)
