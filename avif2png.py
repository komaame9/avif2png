import pillow_avif
from PIL import Image
import sys

print(sys.argv)

filename = ""
for arg in sys.argv:
    if arg.endswith(".avif"):
        filename_src = arg
        filename_dst = filename_src.replace(".avif", ".png", -1)
        
        image = Image.open(filename_src)
        image.save(filename_dst)
        print('saved' + filename_dst)

