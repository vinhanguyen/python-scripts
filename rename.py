# sudo apt install mediainfo python3-pymediainfo

from pathlib import Path
from pymediainfo import MediaInfo
import shutil

downloads = Path.home()/'Downloads'

imgs = list(downloads.glob('IMG_*'))
imgs.sort(key=lambda p: p.stem)

for path in imgs:
    suffix = path.suffix
    info = MediaInfo.parse(path)
    date = [t.recorded_date.split('T')[0] for t in info.tracks if t.track_type == 'General'][0]
    
    name = downloads/f'{date}{suffix}'
    i = 1
    while name.exists():
        name = downloads/f'{date}-{i}{suffix}'
        i += 1
    
    shutil.move(path, name)
