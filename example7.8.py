import json
from pathlib import Path
settings = {'language': 'Python', 'autosave': True}
path = Path('preferences_demo.json')
path.write_text(json.dumps(settings, indent=2), encoding='utf-8')
print(json.loads(path.read_text(encoding='utf-8'))['language'])

