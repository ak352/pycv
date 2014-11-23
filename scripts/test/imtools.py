from PIL import Image
from pylab import *


def histeq(im, nbins=256):
    imhist, bins = histogram(im.flatten(), nbins, normed=True)
    cdf0 = imhist.cumsum()
    cdf = 255 * cdf0/cdf0[-1]
    im2 = interp(im.flatten(), bins[:-1], cdf)

    #Norm cdf to compare with cdf0
    cdf = cdf/cdf[-1]
    return im2.reshape(im.shape) , cdf, cdf0, bins
