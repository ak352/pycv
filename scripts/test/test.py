from PIL import Image
from pylab import *
import sys
import imtools

imo = Image.open(sys.argv[1])
im = array(imo.convert('L'))
im2, cdf, cdf0, bins = imtools.histeq(im)
#print Image.fromArray(im)
#imshow(Image.fromarray(uint8(im)))

subplot(2,2,1)
plot(bins[:-1], cdf0)
subplot(2,2,2)
plot(bins[:-1], cdf)
subplot(2,2,3)
imshow(Image.fromarray(im).convert('LA'))
subplot(2,2,4)
imshow(Image.fromarray(im2).convert('LA'))
show()


