import pandas as pd

df = pd.read_csv("data/applesupport_customer.csv")

# Show 100 random customer messages
sample = df["text"].sample(100, random_state=42)

for i, text in enumerate(sample, 1):
    print(f"{i}. {text}")