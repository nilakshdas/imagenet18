try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO as BytesIO
from PIL import Image


class JPEGCompress(object):
    def __init__(self, quality=75):
        self.quality = quality

    def __call__(self, img):
        out = BytesIO()
        img.save(out, format='JPEG', quality=self.quality)
        return Image.open(out)

    def __repr__(self):
        return self.__class__.__name__ + '(quality={0})'.format(self.quality)
