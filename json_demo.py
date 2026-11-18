import json
from pathlib import Path
report = {"month": "November", "sales": 2500, "orders": 32}
Path("report.json").write_text(
json.dumps(report, indent=2), encoding="utf-8")
loaded = json.loads(Path("report.json").read_text(encoding="utf-8"))

print(loaded["month"], loaded["orders"])

