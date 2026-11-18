from pathlib import Path
path = Path('demo_log.txt')
path.write_text('Started\nFinished\n', encoding='utf-8')
print(path.read_text(encoding='utf-8'))

