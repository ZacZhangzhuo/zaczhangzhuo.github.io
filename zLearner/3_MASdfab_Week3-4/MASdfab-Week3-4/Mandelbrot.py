import math
import Rhino.Geometry as rg
import zorse

DIM = 2
scale = 100
mandelbrot = []


class Spherical(object):
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi


def spherical(x, y, z):
    r = math.sqrt(x * x + y * y + z * z)
    theta = math.atan2(math.sqrt(x * x + y * y), z)
    phi = math.atan2(y, x)
    return Spherical(r, theta, phi)


for i in range(DIM):
    for j in range(DIM):
        edge = False
        for k in range(DIM):

            x = zorse.Remap(i, 0, DIM, -1, 1)
            y = zorse.Remap(j, 0, DIM, -1, 1)
            z = zorse.Remap(k, 0, DIM, -1, 1)

            zeta = zorse.zVector(0, 0, 0)
            iteration = 0
            maxIteration = 10
            n = 8
            while True:

                sphericalZ = spherical(zeta.X, zeta.Y, zeta.Z)
                newx = (
                    math.pow(sphericalZ.r, n)
                    * math.sin(sphericalZ.theta * n)
                    * math.cos(sphericalZ.phi * n)
                )

                newy = (
                    math.pow(sphericalZ.r, n)
                    * math.sin(sphericalZ.theta * n)
                    * math.sin(sphericalZ.phi * n)
                )
                
                newz = math.pow(sphericalZ.r, n) * math.cos(sphericalZ.theta * n)
                zeta.X = newx + x
                zeta.Y = newy + y
                zeta.Z = newz + z

                iteration = iteration + 1

                # if (sphericalZ.r) > 16:
                    # print("x")
                    # if edge:
                        # edge = False
                    # print (str(i)+'x'+str(j)+'x'+str(k))
                    # break
                # print(iteration > maxIteration)
                if iteration > maxIteration:

                    if ~edge:
                        edge = True
                        # print ('x')
                        mandelbrot.append(zorse.zVector(scale * x, scale * y, scale * z))
                    # print(sphericalZ.r)
                    break

pts = []
for vec in mandelbrot:
    pts.append(rg.Point3d(vec.X, vec.Y, vec.Z))
    # print(vec)

outTemp = pts



