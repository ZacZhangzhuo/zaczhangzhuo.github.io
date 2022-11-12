# This script is to generate a flag animation

# Import 
import scriptcontext as sc
import Rhino.Geometry as rg
import copy
import math
import Rhino.Geometry.Brep as rb

# Initial variables
flagLength = 500 #mm
flagWidth = 500 #mm
subdivision = 10 #Must be integer
reset = False #In case to initialize

# Wave the flag
def waveFlag (FlagLength, FlagWidth,Amplitude, Subdivision):
    if "wavingVariable" not in sc.sticky or reset:
        sc.sticky["wavingVariable"] = []
        for i in range(subdivision): 
            sc.sticky["wavingVariable"].append(rg.Point3d((FlagLength/(Subdivision-1))*i,math.sin(math.pi * Subdivision/(i+1)) * Amplitude, 0) ) 
    else:
        for i in range (len(sc.sticky["wavingVariable"])):
            tempPointI = copy.deepcopy(sc.sticky["wavingVariable"][i]) 
            if  i == len (sc.sticky["wavingVariable"])-1:
                tempPoint0 = copy.deepcopy(sc.sticky["wavingVariable"][0]) 
                sc.sticky["wavingVariable"][i] = rg.Point3d(tempPointI.X,tempPoint0.Y, 0 ) 
            else: 
                tempPointJ =copy.deepcopy(sc.sticky["wavingVariable"][i+1])  
                sc.sticky["wavingVariable"][i]  = rg.Point3d(tempPointI.X,tempPointJ.Y, 0 )
    return sc.sticky["wavingVariable"]

# Output flag
flagPoints1 =  waveFlag( flagLength, flagWidth, 10, subdivision)
flagLine1 = rg.NurbsCurve.Create(False, 2, flagPoints1)
flagPoints2 = []
for i in flagPoints1:
    flagPoint2 = rg.Point3d(i.X, i.Y, flagWidth)
    flagPoints2.append(flagPoint2) 
flagLine2 =  rg.NurbsCurve.Create(False, 2, flagPoints2)

Flag = rg.NurbsSurface.CreateRuledSurface(flagLine1,flagLine2 )

# Make a cross on the flag
Patterns.append(Patterns[0])
line = rg.PolylineCurve(Patterns) #Cross line
surface = rg.Surface.CreateExtrusion(line, rg.Vector3d(0,300,0)) 
b1 = rb.CreateFromSurface(surface)
b2 = rb.CreateFromSurface(Flag)
splitted = rb.Split(b2, b1, 0.01)


Flag = splitted[0]
Cross = splitted[1]