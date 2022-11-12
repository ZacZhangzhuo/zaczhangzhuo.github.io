# type: ignore

import Rhino.Geometry as rg
import math
import Rhino
import molazzzz

rule1_predecessor = "X"
rule1_successor = "F+[[X]-X]-F[-FX]+X"
rule2_predecessor = "F"
rule2_successor = "FF"

genotype = "X"


for i in range(Iteration):
    genotype = genotype.replace(rule1_predecessor, rule1_successor)
    genotype = genotype.replace(rule2_predecessor, rule2_successor)

vt = rg.Point3d(0, 0, 0)

vertices = []
Angles = []
lines = []

for c in genotype:
    if c == "+":
        # Turn right
        Angle -= Rotation
    elif c == "-":
        # Turn left
        Angle += Rotation
    elif c == "F":
        # Forward
        rad = math.radians(Angle)
        next_vt = rg.Point3d(Length * math.cos(rad) + vt.X, Length * math.sin(rad) + vt.Y, 0)
        lines.append(rg.Line(vt, next_vt))

        vt = next_vt

    elif c == "[":
        # Save position
        vertices.append(vt)
        Angles.append(Angle)
    elif c == "]":
        # Restore position
        vt = vertices.pop()
        Angle = Angles.pop()

L_system = lines
