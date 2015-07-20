### Homography

1. ```make_homog(x)``` converts the set of points in x to homogeneous coordinates.
2. ```H_from_points(fp, tp)``` finds a homography H such that fp maps to tp using the DLT (direct linear transform) method.
   * First step is to condition points? Why condition points?
   * Create a (2*number of correspondences) by 9 matrix for SVD
   * svd(A) = USV*, where V is reshaped to a 3 by 3 matrix to get the H (homography matrix). Why? Example?
   * Deconditioning step
   * Normalise H
   