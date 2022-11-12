import Rhino.Geometry as rg
import random
import scriptcontext as sc

if "Time" not in sc.sticky or Reset:
    sc.sticky["Time"] = 0

time = sc.sticky["Time"]
sc.sticky["Time"] = sc.sticky["Time"] + 1


class Bouncy:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        self.pts = [self.p]

    def sphereMove(self, bound): #! Zac Add this function
        self.v += self.a
        self.p += self.v
        if self.p.DistanceTo(rg.Point3d(0, 0, 0)) > bound: # Zac. If the point touches the boundary
            normal = rg.Vector3d(self.p.X, self.p.Y, self.p.Z) #Zac. Find the normal of the surface 
            
            temp = self.v.Length
            rg.Vector3d.Unitize(normal)  #Zac. Let length =1
            rg.Vector3d.Unitize(self.v) #Zac. Let length =1
            self.v = self.v - 2 * (self.v * normal) * normal #R = I -2(I*N)N
            
            rg.Vector3d.Unitize(self.v) #After bouncing back, the velocity (v.Length()) of the balls should be the same as the one before bounce
            self.v *= temp 
            
            self.p += self.v #Once touch the boundary, jump back immediately. 

        self.pts.append(self.p)

    def draw_path(self):
        if len(self.pts) >= 2:
            return rg.Curve.CreateInterpolatedCurve(self.pts, 1)
        else:
            return

    def draw_sphere(self):
        return rg.Sphere(self.p, 3)

random.seed(0)
bouncies = []
for _ in range(count):
    bouncy = Bouncy(
        rg.Point3d(0, 0, 0),
        rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)),
        force,
    )
    bouncies.append(bouncy)
for _ in range(time):
    for bouncy in bouncies:
        bouncy.sphereMove(boundary) #! Zac Change from  bouncy.Move(boundary)
trajectories = []
spheres = []
for bouncy in bouncies:
    trajectories.append(bouncy.draw_path())
    spheres.append(bouncy.draw_sphere())