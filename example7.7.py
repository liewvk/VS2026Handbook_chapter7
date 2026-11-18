import csv
from pathlib import Path
rows = [{'item': 'Pen', 'qty': 10}, {'item': 'Pad', 'qty': 4}]
with Path('stock_demo.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['item', 'qty'])
    writer.writeheader()
    writer.writerows(rows)
print('Saved', len(rows), 'products')

