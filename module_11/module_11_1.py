import sys
import requests
from PIL import Image
from PIL import ImageDraw, ImageFont


# Получить изображение
im_url = r'https://i.pinimg.com/736x/9f/96/b5/9f96b5dc3700f5a21786cfc91b8f1508.jpg'

try:
    obj = requests.get(im_url, stream=True).raw
except requests.exceptions.RequestException as e:
    sys.exit(1)

try:
    img = Image.open(obj)
except IOError:
    print('Невозможно открыть изображение!')
    sys.exit(1)

# Обработка
x, y = img.size
kf = 0.5
x, y = int(x * kf), int(y * kf)
f_size = int(28 * kf)
t_shf = int(15 * kf)
img = img.resize((x,y), reducing_gap=3)

img_draw = ImageDraw.ImageDraw(img)
text = f'Лисичка\nразмер {x}x{y}'
font = ImageFont.truetype("arial.ttf", f_size, encoding='utf-8')

img_draw.text((t_shf,t_shf), text, font=font, fill=True)
img.show()


