#图片格式转换
from __future__ import print_function
from PIL import Image

im = "test.jpg"
imout = "test.png"
try:
    Image.open(im).save(imout)
except IOError:
    print("cannot convert", im)