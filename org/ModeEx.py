#模式转换
from __future__ import print_function
from PIL import Image


imin = "test.jpg"
im = Image.open(imin)

cmyk = im.convert("CMYK")#C：Cyan = 青色;M：Magenta = 品红色;Y：Yellow = 黄色;K：Key Plate(blacK) = 定位套版色（黑色）
cmyk.show()
gray = im.convert("L")
gray.show()
