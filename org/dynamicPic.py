from __future__ import print_function
import os, sys
from PIL import Image

infile = "test.gif"

im = Image.open(infile)

im.seek(0)

try:
    while 1:
        im.seek(im.tell()+1)
        im.save(str(im.tell()+1)+".gif")
except EOFError:
    pass