from scipy.ndimage import filters
from PIL import Image
from pylab import *
import sys


def compute_harris_response(im, sigma=3):
    """ Compute the Harris corner detector response function for each pixel 
    in a grayscale image """
    
    # Derivatives
    imx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (0,1), imx)
    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (1,0), imy)
    
    # Compute components of Harris matrix
    # Why gaussian filter is applied again? 
    # To reduce sensitivity to noise at the level of the image and the derivatives
    Wxx = filters.gaussian_filter(imx*imx, sigma)
    Wxy = filters.gaussian_filter(imx*imy, sigma)
    Wyy = filters.gaussian_filter(imy*imy, sigma)
    
    # determinant and trace
    Wdet = Wxx * Wyy - Wxy**2
    Wtr = Wxx + Wyy
    
    return Wdet/Wtr


def get_harris_points(harrisim, min_dist = 10, threshold = 0.1):
    """ Return corners from a Harris response image
    min_dist is the minimum number of pixels separating corners
    and image boundary """
    
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1 #Why times 1? To convert from Boolean matrix?

    # get coordinates of candidates
    coords = array(harrisim_t.nonzero()).T
    candidate_values = [harrisim[c[0],c[1]] for c in coords]
    index = argsort(candidate_values)
    
    #print "coords = ", coords

    allowed_locations = zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1
    
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i,0], coords[i,1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[coords[i,0]-min_dist:coords[i,0]+min_dist,
                              coords[i,1]-min_dist:coords[i,1]+min_dist] = 0
    return filtered_coords

if __name__=="__main__":
    infiles = []
    num_pics = 1
    infiles = ["../../data/lab.jpg"]
    #for k in range(5040,5040+num_pics): #5050):
    #    infiles.append("/Users/abhimanyu.krishna/Pictures/Bali Malaysia Singapore 2014/IMG_%s.JPG" % str(k))
        
    figure()
    gray()
    k = 0
    for infile in infiles:
        print infile
        img = array(Image.open(infile).convert('L'))
        harrisim = compute_harris_response(img)
        filtered_coords = get_harris_points(harrisim, 6)
    
        k+=1
        subplot(2,(num_pics+1)/2,k)
        imshow(img)
        plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords], '*')
        axis('off')
    show()

    

