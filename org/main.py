from __future__ import print_function
import os, sys
from PIL import Image

infile = "test.jpg"

im = Image.open(infile)
# print(im.format, im.size, im.mode)

f, e = os.path.splitext(infile)
# print(f,e)
r,g,b  = im.split()
# source = im.split()
# R, G, B = 0, 1, 2
#s = source[0].point(lambda i: i-254)
s = r.point(lambda i: i-254)
g = g.point(lambda i: i-254)
after = Image.merge("RGB",(s,g,b))

after.show()
outfile = f + ".jpg"
after.save("bbb.jpg")

