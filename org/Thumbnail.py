#缩略图
from __future__ import print_function
from PIL import Image

size = (60, 60)

imin = "test.jpg"
imout = "test.thumbnail"

try:
    im = Image.open(imin)
    im.show()
    im.thumbnail(size)
    im.save(imout, "JPEG")
except IOError:
    print("cannot create thumbnail for", imin)

im.show()