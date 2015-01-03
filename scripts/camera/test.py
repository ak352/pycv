from numpy import *
from scipy import *
import camera

K = array([[1000,0,500],[0,1000,300],[0,0,1]])
tmp = camera.rotation_matrix([0,0,1])[:3,:3]
Rt = hstack((tmp, array([[50],[40],[30]])))

print K, Rt
print cam.factor()
