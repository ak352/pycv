import sys
sys.path.append("../homography")
sys.path.append("../camera")
sys.path.append("../local_image_descriptors")
import homography
import camera
import sift
# compute features
im1 = "../../data/book_frontal.JPG"
im2 = "../../data/book_perspective.JPG"

sift.process_image(im1,'../../data/im0.sift')
l0,d0 = sift.read_features_from_file('../../data/im0.sift')
sift.process_image(im2,'../../data/im1.sift')
l1,d1 = sift.read_features_from_file('../../data/im1.sift')
# match features and estimate homography
matches = sift.match_twosided(d0,d1)
ndx = matches.nonzero()[0]
fp = homography.make_homog(l0[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
tp = homography.make_homog(l1[ndx2,:2].T)
model = homography.RansacModel()
H = homography.H_from_ransac(fp,tp,model)

