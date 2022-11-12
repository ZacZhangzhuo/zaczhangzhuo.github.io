# IMPORT
from copy import copy
import Rhino.Geometry as rg
import math
from ghpythonlib.components import ColourRGB
import sys

# INPUTS
# NautilusSize
# PiceSize
# PiceNumber
# Sharpness
# CircleSize
# CircleRotation
SketchParam1 = 80
SketchParam2 = 50
SketchParam3 = 80
outTemp = []

# CLASS
class Nautilus(object):
    # initialize
    def __init__(self, NautilusSize, PiceSize, PiceNumber, Sharpness, CircleSize, CircleRotation):
        self.nautilusSize = NautilusSize
        self.piceSize = PiceSize
        self.piceNumber = PiceNumber
        self.sharpness = Sharpness
        self.circle = CircleSize
        self.circleRotation = CircleRotation
        self.Sketch = Sketch()
        self.SketchPoints = []
        self.SketchLines1 = []
        self.SketchLines2 = []
        self.SketchLines3 = []
        self.SketchLines4 = []
        self.SketchLines5 = []
        self.circles = self.__MakeSpiralCircles(
            self.__MakeSpiralPoints(NautilusSize, PiceSize, PiceNumber, Sharpness),
            CircleSize,
            self.SketchPoints,
        )
        self.coloursU = self.__makeColours()
        self.coloursV = []
        self.objects = self.__makeObjects()

    def __FibonacciSharpness(PiceNumber, Sharpness):
        zSharpness = []
        zSharpness.append(Sharpness)
        zSharpness.append(Sharpness)
        for i in range(PiceNumber - 2):
            zSharpness.append(zSharpness[i] + zSharpness[i + 1])
        return zSharpness

    def __Rotate(self, circle, rotation):
        # circle = rg.Circle(x)
        circle.Transform(
            rg.Transform.Rotation(
                rg.Vector3d(1, 0, 0),
                rg.Vector3d(math.cos(rotation), math.sin(rotation), 0),
                circle.Center,
            )
        )
        return circle

    def __MakeSpiralPoints(self, NautilusSize, PiceSize, PiceNumber, Sharpness):
        # Outcome point3d[]
        points = []
        sketchPoints = []

        for t in range(PiceNumber + SketchParam1):
            r = NautilusSize * t
            x = (
                VarX * r * math.cos(2 * math.pi * t * PiceSize * 0.1)
                + (1 - VarX) * r * 2 * math.pi * t * PiceSize * 0.1
            )
            y = (
                VarY * r * math.sin(2 * math.pi * t * PiceSize * 0.1)
                + (1 - VarY) * r * 2 * math.pi * t * PiceSize * 0.1
            )
            #  ys = FibonacciSharpness(PiceNumber, Sharpness)#! FibonacciSharpness
            #  points.append(rg.Point3d(x,y,ys[t]))#! FibonacciSharpness
            #  print ys
            if t < PiceNumber:
                points.append(rg.Point3d(x, y, Sharpness * t * t))

            sketchPoints.append(rg.Point3d(x, y, Sharpness * t * t))

        # * Sketch
        if IsSketch:
            self.SketchLines1 = self.Sketch.PointsToCurve(sketchPoints)
        self.SketchPoints = sketchPoints
        self.SketchLines4 = self.Sketch.CurveProjection(self.SketchLines1)
        self.SketchLines5 = rg.Point3d(
            (1 - VarX) * r * 2 * math.pi * t * PiceSize * 0.1,
            (1 - VarY) * r * 2 * math.pi * t * PiceSize * 0.1,
            Sharpness * t * t,
        )
        # self.SketchLines5=self.Sketch.VerticalLines(self.Sketch.PointsToCurve(points), 100)
        return points

    def __MakeSpiralCircles(self, SpiralPoints, Size, SketchPoints):
        circles = []
        
        '''
        for i in range(len(SketchPoints) - SketchParam2 - 1):
            # Make the vector
            vector = rg.Vector3d(SketchPoints[i + 1] - SketchPoints[i])
            # Make the plane
            plane = rg.Plane((SketchPoints[i + 1] + SketchPoints[i]) / 2, vector)

            # Rotate plane #!Hard part
            xAxis = copy(plane.XAxis)
            xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, plane.YAxis))
            plane.Transform(rg.Transform.Rotation(plane.XAxis, xAxis, plane.Origin))
            if plane.YAxis.Z < 0:
                plane = rg.Plane(plane.Origin, -plane.XAxis, -plane.YAxis)
        '''
        vector = rg.Vector3d(SketchPoints[1] - SketchPoints[0]) 
        plane = rg.Plane((SketchPoints[ 1] + SketchPoints[0]) / 2, vector) 
        xAxis = copy(plane.XAxis)
        xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, plane.YAxis))
        plane.Transform(rg.Transform.Rotation(plane.XAxis, xAxis, plane.Origin))
        if plane.YAxis.Z < 0:
            plane = rg.Plane(plane.Origin, -plane.XAxis, -plane.YAxis)
        
        for i in range(len(SketchPoints) - SketchParam2 - 1):
            transform = rg.Transform.Translation(SketchPoints[i + 1] - SketchPoints[i])
            o_plane = copy(plane)
            plane.Transform(transform)
            rotate = rg.Transform.Rotation(o_plane.ZAxis,SketchPoints[i + 1] - SketchPoints[i], plane.Origin )#startDirection: Vector3d, endDirection: Vector3d, rotationCenter: Point3d
            plane.Transform(rotate)

            # outTemp.append(plane)

            # Make circle
            circle = rg.Circle(plane, Size * (i + 1))
            if i < len(SpiralPoints) - 1:
                circles.append(
                    self.__Rotate(circle, (i / (len(SpiralPoints) - 1)) * CircleRotation)
                )
            else:
                # * Sketch
                if IsSketch:
                    self.SketchLines2.append(circle)
            if IsSketch:
                if i < len(SketchPoints) - 1 - SketchParam3 and i % 2 == 0:
                    # print i
                    # print (len(SketchPoints) - 1- SketchParam3)
                    # rg.ArcCurve()
                    self.SketchLines3.append(
                        self.__Rotate(
                            rg.Rectangle3d(
                                plane,
                                rg.Interval(-Size * (i + 1), Size * (i + 1)),
                                rg.Interval(-Size * (i + 1), Size * (i + 1)),
                            ),
                            i / (len(SketchPoints) - 1) * CircleRotation,
                        ).ToPolyline()
                    )

        return circles

    def __makeColours(self):
        Colours = []
        for i in range(len(self.circles) - 1):
            colour = ColourRGB(255, 28, 114, 167)
            Colours.append(colour)
        return Colours

    def __makeObjects(self):
        Nautilus = []
        for i in range(len(self.circles) - 1):
            # Nautilus.append(
            #     rg.NurbsSurface.CreateRuledSurface(
            #         self.circles[i].ToNurbsCurve(), self.circles[i + 1].ToNurbsCurve()
            #     )
            # )
            for t in range(int(math.floor(1 / Tolerance))):
                self.coloursV.append(
                    ColourRGB(
                        150,
                        t / (math.floor(1 / Tolerance)),
                        255 * t / (math.floor(1 / Tolerance)),
                        255,
                    )
                )
                Nautilus.append(
                    rg.PolylineCurve(
                        [
                            self.circles[i].PointAt(t / Tolerance),
                            self.circles[i + 1].PointAt(t / Tolerance),
                        ]
                    )
                )
        return Nautilus


class Sketch(object):
    def PointsToCurve(self, points):
        return rg.NurbsCurve.Create(False, 2, points)

    def CurveProjection(self, Curve):
        # Curve = rg.NurbsCurve()
        return Curve.ProjectToPlane(Curve, rg.Plane.WorldXY)

    def VerticalLines(self, Curve, number):
        points = []
        # Curve = rg.NurbsCurve()
        temp = Curve.DivideByLength(Curve.GetLength() / number, True)
        for para in temp:
            points.append(Curve.PointAt(para))
        return points


nautilus = Nautilus(NautilusSize, PiceSize, PiceNumber, Sharpness, CircleSize, CircleRotation)
Objects = nautilus.objects
ColoursU = nautilus.coloursU
ColoursV = nautilus.coloursV
Circles = nautilus.circles
SketchLines1 = nautilus.SketchLines1
SketchLines2 = nautilus.SketchLines2
SketchLines3 = nautilus.SketchLines3
SketchLines4 = nautilus.SketchLines4
SketchLines5 = nautilus.SketchLines5
