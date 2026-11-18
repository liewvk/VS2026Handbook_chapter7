import json
from pathlib import Path
settings = {'theme': 'dark', 'autosave': True, 'recent': ['invoice.py']}
path = Path('settings.json')
path.write_text(json.dumps(settings, indent=2), encoding='utf-8')
loaded = json.loads(path.read_text(encoding='utf-8'))
print('Theme:', loaded['theme'])
print('Autosave:', loaded['autosave'])

