from pathlib import Path
from shutil import copy2
source = Path('original_note.txt')
source.write_text('Review quarterly sales numbers.\n', encoding='utf-8')
target = Path('backups') / source.name
target.parent.mkdir(exist_ok=True)
copy2(source, target)
print('Backup created:', target.exists())

