from __future__ import print_function
import os, sys
from PIL import Image
from PIL import ImageEnhance

infile = "test.jpg"

im = Image.open(infile)

enh = ImageEnhance.Contrast(im)

enh.enhance(1.3).show("30% more contrast")