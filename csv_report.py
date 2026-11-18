import csv
from pathlib import Path
path = Path('monthly_sales.csv')
rows = [{'month': 'Jan', 'sales': 1200}, {'month': 'Feb', 'sales': 1650}]
with path.open('w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['month', 'sales'])
    writer.writeheader()
    writer.writerows(rows)
with path.open(newline='', encoding='utf-8') as file:
    for row in csv.DictReader(file):
        print(row['month'], row['sales'])

