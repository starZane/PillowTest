#通道分离
from __future__ import print_function
from PIL import Image


imin = "testbig.jpg"
im = Image.open(imin)


r, g, b = im.split()#通道分离
r.show()
g.show()
b.show()

im = Image.merge("RGB", (b, g, r))#b,r通道翻转后合并
im.show()
