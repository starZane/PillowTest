#图片打开及属性查看
from PIL import Image

image = Image.open("test.jpg")

print(image.size,image.format,image.mode)#尺寸，格式，模式

image.show()