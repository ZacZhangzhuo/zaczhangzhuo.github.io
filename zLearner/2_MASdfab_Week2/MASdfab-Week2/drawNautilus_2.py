# IMPORT
from copy import copy
import Rhino.Geometry as rg
import math
from ghpythonlib.components import ColourRGB

# INPUTS
# NautilusSize
# PiceSize
# PiceNumber
# Sharpness
# CircleSize
# CircleRotation

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
        self.circles = self.__MakeSpiralCircles(
            self.__MakeSpiralPoints(NautilusSize, PiceSize, PiceNumber, Sharpness), CircleSize
        )

    def __FibonacciSharpness(PiceNumber, Sharpness):
        zSharpness = []
        zSharpness.append(Sharpness)
        zSharpness.append(Sharpness)
        for i in range(PiceNumber - 2):
            zSharpness.append(zSharpness[i] + zSharpness[i + 1])
        return zSharpness

    def __RotateCircle(self, circle, rotation):
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
        for t in range(PiceNumber):

            r = NautilusSize * t
            x = r * math.cos(2 * math.pi * t * PiceSize * 0.1)
            y = r * math.sin(2 * math.pi * t * PiceSize * 0.1)
            #  ys = FibonacciSharpness(PiceNumber, Sharpness)#! FibonacciSharpness
            #  points.append(rg.Point3d(x,y,ys[t]))#! FibonacciSharpness
            #  print ys
            # points.append(rg.Point3d(x, y, Sharpness * t*t))
            points.append(rg.Point3d(x, y, Sharpness * (inTemp - t) * (inTemp - t)))

        return points

    def __MakeSpiralCircles(self, SpiralPoints, Size):
        circles = []
        for i in range(len(SpiralPoints) - 1):
            # Make the vector
            vector = rg.Vector3d(SpiralPoints[i + 1] - SpiralPoints[i])
            # Make the plane
            plane = rg.Plane((SpiralPoints[i + 1] + SpiralPoints[i]) / 2, vector)

            # Rotate plane #!Hard part
            xAxis = copy(plane.XAxis)
            xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, plane.YAxis))
            plane.Transform(rg.Transform.Rotation(plane.XAxis, xAxis, plane.Origin))
            if plane.YAxis.Z < 0:
                plane = rg.Plane(plane.Origin, -plane.XAxis, -plane.YAxis)

            # Make circle
            circle = rg.Circle(plane, Size * (i + 1))
            # circle = rg.Rectangle3d(plane, rg.Interval(-Size* (i + 1), Size* (i + 1)),rg.Interval(-Size* (i + 1), Size* (i + 1)))
            circles.append(
                self.__RotateCircle(circle, (i / (len(SpiralPoints) - 1)) * CircleRotation)
            )

        return circles

    def colours(self):
        Colours = []
        for i in range(len(self.circles) - 1):
            colour = ColourRGB(
                155,
                i * 255 / (len(self.circles) - 1),
                i * 255 / (len(self.circles) - 1),
                i * 255 / (len(self.circles) - 1),
            )
            Colours.append(colour)
        Colours.reverse()
        return Colours

    def object(self):
        Nautilus = []
        for i in range(len(self.circles) - 1):
            # Nautilus.append(
            #     rg.NurbsSurface.CreateRuledSurface(
            #         self.circles[i].ToNurbsCurve(), self.circles[i + 1].ToNurbsCurve()
            #     )
            # )
            for t in range(int(math.floor(1/Tolerance))):
                Nautilus.append(
                    rg.PolylineCurve([self.circles[i].PointAt(t/Tolerance), self.circles[i+1].PointAt(t/Tolerance)])
                    )
            
        return Nautilus


nautilus = Nautilus(NautilusSize, PiceSize, PiceNumber, Sharpness, CircleSize, CircleRotation)
Objects = nautilus.object()
Colours = nautilus.colours()
Circles = nautilus.circles
