from numpy import *
from scipy import linalg

class Camera(object):
    """ Class for representing pin-hole cameras """
    
    def __init__(self, P):
        self.P = P
        self.K = None
        self.t = None
        self.c = None
        
    def project(self, X):
        """ Project points in X (4*n array) and normalize coordinates. """
        x =  dot(self.P, X)
        for i in range(3):
            x[i] /= x[2]
        return x

    def factor(self):
        """ Factorize the camera matrix into K, R, t as P = K[R|t]. """
        # factor first 3*3 part
        K, R = linalg.rq(self.P[:,:3])
        
        # make diagonal of K positive
        T = diag(sign(diag(K)))
        if linalg.det(T) < 0:
            T[1,1] *= -1
        self.K = dot(K, T)
        self.K = dot(K, T)
        self.R = dot(T, R) # T is its own inverse
        self.t = dot(linalg.inv(self.K), self.P[:,3])
        
    def center(self):
        """ Compute and return the camera center """
        if self.c is not None:
            return self.c
        else:
            # comput c by factoring
            self.factor()
            self.c = -dot(self.R.T, self.t) # Why? See readme.
            return self.c

# helper functions    
def rotation_matrix(a):
    """ Creates a 3D rotation matrix for rotation 
    aorund the axis of the vector a. """
    R = eye(4)
    R[:3, :3] = linalg.expm([[0, -a[2], a[1]], [a[2], 0, -a[0]],[-a[1], a[0], 0]])
    return R

def rq(A):
    from scipy.linalg import qr
    Q, R = qr(flipud(A).T)
    R = flipud(R.T)
    Q = Q.T
    return R[:, ::-1], Q[::-1, :]


def my_calibration(sz):
    row,col = sz
    fx = 2555*col/2592
    fy = 2586*row/1936
    K = diag([fx,fy,1])
    K[0,2] = 0.5*col
    K[1,2] = 0.5*row
    return K    



        
