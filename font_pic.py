#!usr/bin/python
#_*_coding:utf-8_*_
from PIL import Image,ImageFont,ImageDraw
import re
import sys
def identificate_word_or_picture(somefile):
    mattern = r'\S.(jpg|jpeg|gif|png)$'
    if re.compile(mattern).findall(somefile):
        image = Image.open(somefile)
        identification = picture_convert(image)
        identification.show()
    else:
        identification = create_text_picture(somefile)
    return identification
def picture_convert(picture,width=50):
    (picture_width,picture_height) = picture.size
    ratio = picture_height/float(picture_width)
    new_picture_height = int(width * ratio)
#    print new_picture_height
    new_picture = picture.resize((width,new_picture_height))
    return new_picture.convert('L')
def create_text_picture(text):
    text_width = text.__len__()
    font_size = 50 / text_width
    image_height = font_size / 0.7  # 0.7是宋体的宽高比
    im = Image.new('RGB', (50, int(image_height)), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    ft = ImageFont.truetype('Songti.ttc', int(font_size))
    dr.text((0, 0), text, font=ft, fill='black')
    return im.convert('L')
def image2symbol(somefile,data_width=25,image_width=50):
    symbol = ['#','#','#','#','#','#','#',' ',' ',' ',' ']
    image_data = list(identificate_word_or_picture(somefile).getdata())
    symbol_data = []
#    print image_data.__len__()
    for i in image_data:
        symbol_data.append(symbol[i/data_width])
    all_symbol_data = ' '.join(symbol_data)
#    print all_symbol_data.__len__()
    symbol_data_simple = []
    for i in list(xrange(0,all_symbol_data.__len__()+1,image_width*2)):
        symbol_data_simple.append(all_symbol_data[i:image_width*2+i])
    return "\n".join(symbol_data_simple)
text_test = sys.argv[1].decode('utf-8')

a = image2symbol(text_test)
print a

