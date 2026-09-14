import pandas as pd

df = pd.read_csv("data/applesupport_customer.csv")

print("Total customer messages:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nSample customer messages:")
print(df["text"].sample(10, random_state=42).to_string(index=False))