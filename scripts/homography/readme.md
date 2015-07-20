### Homography


```test_book.py`` takes SIFT features from a frontal view of a book and a perspective view of the same book and computes the homography from the SIFT matches.

```homography.py```
1. ```make_homog(x)``` converts the set of points in x to homogeneous coordinates.
2. ```H_from_points(fp, tp)``` finds a homography H such that fp maps to tp using the DLT (direct linear transform) method.
   * First step is to condition points? Why condition points?
   * Create a (2*number of correspondences) by 9 matrix for SVD
   * svd(A) = USV*, where V is reshaped to a 3 by 3 matrix to get the H (homography matrix). Why? Example?
   * Deconditioning step
   * Normalise H

### RANSAC
```ransac.py```
Given:
    data - a set of observed data points
    model - a model that can be fitted to data points
    n - the minimum number of data values required to fit the model
    k - the maximum number of iterations allowed in the algorithm
    t - a threshold value for determining when a data point fits a model
    d - the number of close data values required to assert that a model fits well to data
Return:
    bestfit - model parameters which best fit the data (or nil if no good model is found)
