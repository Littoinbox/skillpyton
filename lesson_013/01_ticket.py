# -*- coding: utf-8 -*-
import argparse
import os

from PIL import Image, ImageDraw, ImageFont, ImageColor


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(fio, from_, to, date, save_to):
   tmp_img = os.path.join('images', 'ticket_template.png')
   im = Image.open(tmp_img)
   font_path = os.path.join('python_snippets', 'fonts', 'Cruinn.ttf')
   draw = ImageDraw.Draw(im)
   font = ImageFont.truetype(font_path, size=16)
   y = 0 + 75 + (10 + font.size) * 2
   message = f'{fio}'
   draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])
   y = 0 + 140 + (10 + font.size) * 2
   message = f'{from_}'
   draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])
   y = 0 + 210 + (10 + font.size) * 2
   message = f'{to}'
   draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])
   y = 0 + 210 + (10 + font.size) * 2
   message = f'{date}'
   draw.text((290, y), message, font=font, fill=ImageColor.colormap['black'])
   save_path = os.path.join(save_to, fio+'tiket.jpg')
   rgb_img  = im.convert("RGB")
   rgb_img.save(save_path)
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


if __name__ == '__main__':
   parser = argparse.ArgumentParser(
      prog='tiket',
      description='Create tiket',
      epilog='Text at the bottom of help'
   )
   parser.add_argument('-f', '--fio')
   parser.add_argument('--frome')
   parser.add_argument('--to')
   parser.add_argument('--date')
   parser.add_argument('--save_to')
   args = parser.parse_args()
   make_ticket(args.fio, args.frome , args.to, args.date, args.save_to)