import mola
from mola import module_rhino
import Rhino.Geometry as rg
import Rhino.Geometry.Intersect as intersection
import zorse
import csv
import math


def Distance(vertex1, vertex2):
    return math.pow(
        math.pow(vertex1.x - vertex2.x, 2)
        + math.pow(vertex1.y - vertex2.y, 2)
        + math.pow(vertex1.z - vertex2.z, 2),
        0.5,
    )

DIM32 = Location
#DIM32 = r"C:\Zac\19 Github\Notes\MASdfab-Week5\DIM32.csv"
#DIM64 = r"C:\Zac\19 Github\Notes\MASdfab-Week5\DIM64.csv"
#DIM128 = r"C:\Zac\19 Github\Notes\MASdfab-Week5\DIM128.csv"

data = []
with open(DIM32) as f:
    reader = csv.reader(f)
    # headers = next(reader)
    for row in reader:
        data.extend(row)


dim = int(math.floor(len(data) ** (1 / 3) + 1))


# ! Too tree
facesArray = []
lineArray = []
for i in range(dim):
    facesArray.append(data[dim * dim * i : dim * dim * (i + 1)])

for face in facesArray:
    tempArray = []
    for i in range(dim):
        tempArray.append(face[dim * i : dim * (i + 1)])
    lineArray.append(tempArray)
# ! End to tree

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            lineArray[0][j][k] = 0
            lineArray[-1][j][k] = 0
            lineArray[i][0][k] = 0
            lineArray[i][-1][k] = 0
            lineArray[i][j][0] = 0
            lineArray[i][j][-1] = 0


# ! Too list
values = []
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            values.append(int(lineArray[i][j][k]))

cubes = mola.mesh_marching_cubes(dim, dim, dim, values, 0.5)

# Marching cubes mesh to the center
for vertex in cubes.vertices:
    vertex.x = vertex.x - dim / 2
    vertex.y = vertex.y - dim / 2
    vertex.z = vertex.z - dim / 2


# Get the minimal distance
Center = mola.Vertex(0, 0, 0)
distance = Distance(Center, cubes.vertices[0])
for vertex in cubes.vertices:
    if Distance(Center, vertex) <= distance:
        distance = Distance(Center, vertex)

test = []
for vertex in cubes.vertices:
    vec = rg.Vector3d(vertex.x, vertex.y, vertex.z)
    vec.Unitize()
    ray = rg.Ray3d(rg.Point3d(0, 0, 0), vec)
    
    intersectionPoint = intersection.Intersection.MeshRay(inTemp, ray)
    if intersectionPoint == float('inf')  or intersectionPoint == float( '-inf'): intersectionPoint =0
    # if intersectionPoint ==
    test.append(intersectionPoint)
    
    intersectionPoint = ray.PointAt(intersectionPoint - distance)  # type: ignore
    
    vertex.x = intersectionPoint.X + vertex.x
    vertex.y = intersectionPoint.Y + vertex.y
    vertex.z = intersectionPoint.Z + vertex.z


# Roughness
for vertex in cubes.vertices:
    vec = rg.Vector3d(vertex.x, vertex.y, vertex.z)
    vec.Unitize()
    ray = rg.Ray3d(rg.Point3d(0, 0, 0), vec)
    intersectionPoint = intersection.Intersection.MeshRay(inTemp, ray)
    if intersectionPoint == float('inf')  or intersectionPoint == float( '-inf'): intersectionPoint =0
    intersectionPoint = ray.PointAt(intersectionPoint)  # type: ignore
    vertex.x += (vertex.x - intersectionPoint.X) * xRoughness
    vertex.y += (vertex.y - intersectionPoint.Y) * yRoughness
    vertex.z += (vertex.z - intersectionPoint.Z) * zRoughness



cubes.update_topology()

# Color code
colorPara = []
greatestNumber = 0
smallestNumber = 1000000000000000000000000000000000000000000
for face in cubes.faces:
    para = Distance(face.center(), Center)
    colorPara.append(para)
    if para > greatestNumber:
        greatestNumber = para
    if para < smallestNumber:
        smallestNumber = para


colors = []
for i in range(len(colorPara)):
    para = int((colorPara[i] - smallestNumber) / (greatestNumber - smallestNumber) * 10)
    colors.append([Colors[para].R/255, Colors[para].G/255, Colors[para].B/255])
    cubes.faces[i].color =colors [i]


outTemp = module_rhino.display_mesh(cubes)
