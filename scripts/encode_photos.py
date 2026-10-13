"""Export JPEG pentru web/PDF; păstrează dimensiunile și originalele PNG."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
for name in ('fotografii-caz','plic-recuperat'):
    with Image.open(ROOT/'output/imagegen'/f'{name}.png') as image:
        image.convert('RGB').save(ROOT/'platforma/offline/assets/plic'/f'{name}.jpg',quality=93,optimize=True,subsampling=0)
print('Exportate 2 fotografii JPEG; originale PNG pastrate.')
