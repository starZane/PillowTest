#像素点处理
from __future__ import print_function
from PIL import Image


imin = "test.jpg"
im = Image.open(imin)
im.show()
out = im.point(lambda i: i * 2)
out.show()