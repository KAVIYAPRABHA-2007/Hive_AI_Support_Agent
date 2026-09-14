import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

replies = pd.read_csv(BASE_DIR / "data" / "applesupport_replies.csv")

replies = replies.dropna(subset=["text"])
replies = replies.head(5000)

output_file = BASE_DIR / "data" / "support_knowledge_base.csv"

replies.to_csv(output_file, index=False)

print("Knowledge base created!")
print("Historical replies:", len(replies))
print("Saved to:", output_file)