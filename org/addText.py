from __future__ import print_function
import os, sys
from PIL import Image
from PIL import PSDraw

infile = "test.jpg"

im = Image.open(infile)

title = "test"
pix = 72
box = (1 * pix, 2 * pix, 7 * pix, 10 * pix)

ps = PSDraw.PSDraw()  # default is sys.stdout
ps.begin_document(title)

# draw the image (75 dpi)
ps.image(box, im, 75)
ps.rectangle(box)

# draw centered title
ps.setfont("HelveticaNarrow-Bold", 36)
w, h, b =  20,20,20
ps.text((4 * 72 - w / 2, 1 * 72 - h), title)

ps.end_document()

im.show()
