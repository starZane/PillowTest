from PIL import TarIO
from PIL import Image
fp = TarIO.TarIO("test.tar", "test.jpg")
im = Image.open(fp)

im.show()
