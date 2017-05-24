from __future__ import print_function
from PIL import Image

infile = "test.jpg"
im = Image.open(infile)
print("original =", im.mode, im.size)

im.draft("L", (100, 100))
print("draft =", im.mode, im.size)
im.save("draft.jpg")
im.show()