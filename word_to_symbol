#!usr/bin/python
#_*_coding:utf-8_*_
from PIL import Image,ImageFont,ImageDraw
def create_text_picture(text):
    text_width = text.__len__()
    font_size = 100 / text_width
    image_height = font_size / 0.7  # 0.7是宋体的宽高比
    im = Image.new('RGB', (100, int(image_height)), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    ft = ImageFont.truetype('Songti.ttc', int(font_size))
    dr.text((0, 0), text_test, font=ft, fill='black')
    return im.convert('L')
def image2symbol(text,data_width=25,image_width=100):
    symbol = ['@','#','$','%','^','&','*','!','~',' ',' ']
    image_data = list(create_text_picture(text).getdata())
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

print "Please input something:"
text_test = raw_input().decode('utf-8')
a = image2symbol(text_test)
print a

