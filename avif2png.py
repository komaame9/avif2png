import pillow_avif
from PIL import Image
import sys

print(sys.argv)

filename = ""
for arg in sys.argv:
    if arg.endswith(".avif"):
        filename = arg
        image = Image.open(filename);
        image.save(filename + ".png");
        print('saved' + filename + ".png")

