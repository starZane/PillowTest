#图片增强：加强滤镜
from __future__ import print_function
from PIL import Image,ImageFilter


imin = "test.jpg"
im = Image.open(imin)
im.show()
out = im.filter(ImageFilter.DETAIL)
out.show()