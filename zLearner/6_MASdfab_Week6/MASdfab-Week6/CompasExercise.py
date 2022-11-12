import json
import os
import Rhino.Geometry as rg
import compas
from compas_rhino import conversions as c

# myJson = ' { "student": "Paul","laptop": "Lenovo", "Tag": ["Github", "Hiking"]}'
# myJson = json.loads(myJson)
# # print (type(myJson))

# ghCanvas = ghenv.Component.OnPingDocument()
# folder = os.path.dirname(ghCanvas.FilePath)
# # print (folder)

# with open(os.path.join(folder, "simple_spheres.json")) as file:
#     myD = json.load(file)

# rr = myD["radius"]
# xx = myD["originX"]
# yy = myD["originY"]
# zz = myD["originZ"]

# Spheres = []
# for x, y, z, r in zip(xx, yy, zz, rr):
#     s = rg.Sphere(rg.Plane(rg.Point3d(x,y,z), rg.Vector3d.ZAxis), r)  # type: ignore
#     Spheres.append(s)

# outTemp = Spheres
p = rg.Plane(rg.Point3d(10, 10, 10), rg.Vector3d.ZAxis)


# ps = [rg.Plane(rg.Point3d(10,10,10), rg.Vector3d.ZAxis)]
x = rg.Vector3d.ZAxis
rg.Vector3d(x)
rg.Point3d(rg.Vector3d(0, 0, 0))
# rg.Plane()
originFrames = [c.plane_to_compas_frame(p) for p in ps]
outTemp = originFrames
# print(rr)

# with open(os.path.join(folder, "myFistItem"), "w") as file:
# myJ = json.dump(myJson, file, indent=2)
