import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

kb = pd.read_csv(BASE_DIR / "data" / "support_knowledge_base.csv")

def find_examples(query, n=3):
    words = set(str(query).lower().split())

    def score(text):
        text_words = set(str(text).lower().split())
        return len(words & text_words)

    kb["score"] = kb["text"].apply(score)
    results = kb.sort_values("score", ascending=False).head(n)

    return results[["text", "score"]]

if __name__ == "__main__":
    query = input("Customer message: ")

    examples = find_examples(query)

    print("\nSimilar historical AppleSupport replies:\n")

    for _, row in examples.iterrows():
        print("-", row["text"])
        print("  Match score:", row["score"])
