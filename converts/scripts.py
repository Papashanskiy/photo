import os
from PIL import Image


def convert_to_jpeg(filename):
    f, e = os.path.splitext(filename)
    outfile = f + '.jpeg'
    if filename != outfile:
        try:
            Image.open(filename).save(outfile)
        except IOError:
            return 'Cannot convert'
