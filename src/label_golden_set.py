import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "golden_set" / "labeling_sample.csv"
output_file = BASE_DIR / "golden_set" / "golden_set.csv"

df = pd.read_csv(input_file)

df["intent"] = ""

df.to_csv(output_file, index=False)

print("Golden set created!")
print("Rows:", len(df))
print("File:", output_file)