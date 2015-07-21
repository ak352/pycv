


## Camera
 * project - Projects a 4 by N matrix (set of 3D points in homogeneous coordinates) to 3 by N (set of 2D points)
 * factor - Factorize the camera matrix into K, R, T as P = K[R|T], where P is 3x4, K, the intrinsic camera parameters, is 3x4, and [R|t] is 4x4. Since K is a triangular matrix, the factorisation is done using QR factorisation of KR.
 * center - returns the camera centre by -Rt*T. [R|T] brings a point from world coordinates to camera coordinates.
 ```
 [R|T][x, y, z, 1]t = [0,0,0,1]
 In Cartesian coordinates, this becomes - 
 R[x,y,z]t + T = 0
 [x,y,z]t = -Rt*T ... this should be a 3x1 vector
 ```
 * rotation_matrix - rotates points around a line [a[0], a[1], a[2]] by creating the rotation matrix by taking the expm() of the following matrix -
   ```
   |0	-a[2]	 a[1]|
   |a[2] 0	-a[0]|
   |-a[1] a[0]     0 |
   ```
 