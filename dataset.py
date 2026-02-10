import pandas as pd

# Load CSV
df = pd.read_csv("gate_questions_60.csv")

# Convert to JSON
df.to_json("questions.json", orient="records", indent=2)
print("✅ Conversion done! File saved as questions.json")
