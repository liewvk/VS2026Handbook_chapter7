import csv
from pathlib import Path
path = Path("sales.csv")
rows = [{"item": "Pen", "amount": 10},
{"item": "Book", "amount": 25}]
with path.open("w", newline="", encoding="utf-8") as file:
 writer = csv.DictWriter(file, fieldnames=["item", "amount"])
 writer.writeheader()
 writer.writerows(rows)
with path.open(newline="", encoding="utf-8") as file:
 total = sum(float(row["amount"])
for row in csv.DictReader(file))
print("Total:", total)

