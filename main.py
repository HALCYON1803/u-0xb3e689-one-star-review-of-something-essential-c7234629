import os

os.makedirs("/output", exist_ok=True)

# One deadpan one-star review of sleep, in the voice of a long-suffering
# customer: loyal use, the same defect every morning, no refund.
PARTS = [
    "Thirty years of sleep. Still wake up tired every morning.",
    "No refund offered.",
    "Would not recommend.",
]
LINE = " ".join(PARTS)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
