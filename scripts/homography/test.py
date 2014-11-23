from numpy import *
import homography

f = array(([1,1], [2,1], [3,2], [4,4]))
t = f+1
f = f.T
f = homography.make_homog(f)
t = t.T
t = homography.make_homog(t)


#print f, t
print homography.H_from_points(f,t)
