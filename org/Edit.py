#图片编辑：裁剪、翻转、粘贴、合并
from __future__ import print_function
from PIL import Image


imin = "testbig.jpg"
im = Image.open(imin)
im.show()
box = (100, 100, 800, 800)  # 设置要拷贝的区域

# 将im表示的图片对象拷贝到region中，大小为(400*400)像素。这个region可以用来后续的操作(region其实就是一个Image对象)，box变量是一个四元组(左，上，右，下)。
region = im.crop(box)

region = region.transpose(Image.ROTATE_180)  # 从字面上就可以看出，先把region中的Image反转180度，然后再放回到region中。
im.paste(region, box)  # 粘贴box大小的region到原先的图片对象中。

im.show()