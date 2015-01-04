import sys
sys.path.append("../homography")
sys.path.append("../camera")
sys.path.append("../local_image_descriptors")
import homography
import camera
import sift
import cube
from numpy import *

# compute features                                                        
sift.process_image('../../data/book_frontal.JPG','../../data/im0.sift')
l0,d0 = sift.read_features_from_file('../../data/im0.sift')
sift.process_image('../../data/book_perspective.JPG','../../data/im1.sift')
l1,d1 = sift.read_features_from_file('../../data/im1.sift')
# match features and estimate homography                                        
matches = sift.match_twosided(d0,d1)
ndx = matches.nonzero()[0]
fp = homography.make_homog(l0[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
tp = homography.make_homog(l1[ndx2,:2].T)
model = homography.RansacModel()
H,ransac_data = homography.H_from_ransac(fp,tp,model)


# camera calibration
K = camera.my_calibration((747,1000))
# 3D points at plane z=0 with sides of length 0.2
box = cube.cube_points([0,0,0.1],0.1)
# project bottom square in first image
cam1 = camera.Camera( hstack((K,dot(K,array([[0],[0],[-1]])) )) )
# first points are the bottom square
box_cam1 = cam1.project(homography.make_homog(box[:,:5]))
# use H to transfer points to the second image
print dot(H,box_cam1)
box_trans = homography.normalize(dot(H,box_cam1))
# compute second camera matrix from cam1 and H
cam2 = camera.Camera(dot(H,cam1.P))
A = dot(linalg.inv(K),cam2.P[:,:3])
A = array([A[:,0],A[:,1],cross(A[:,0],A[:,1])]).T
cam2.P[:,:3] = dot(K,A)
# project with the second camera
box_cam2 = cam2.project(homography.make_homog(box))
# test: projecting point on z=0 should give the same
point = array([1,1,0,1]).T
print homography.normalize(dot(dot(H,cam1.P),point))
print cam2.project(point)

import pickle
with open('../../data/ar_camera.pkl','w') as f:
    pickle.dump(K,f)
    pickle.dump(dot(linalg.inv(K),cam2.P),f)
