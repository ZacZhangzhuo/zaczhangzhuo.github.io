# Import 
from cgitb import reset
import scriptcontext as sc
import Rhino.Geometry as rg
import copy
import math
import Rhino.Geometry.Brep as rb

#Def
class Star:
    def __init__(self,xpos,ypos,rad,peaks,f,c=(255,0,0,0)):
        self.xpos = xpos
        self.ypos = ypos
        self.rad = rad
        self.peaks = peaks
        self.factor = f
    
    def draw(self):
        pts_star = []
        res = self.peaks * 2
        theta = 2 * math.pi / res
        
        for i in range(res):
            if i%2 == 0:
                radius = self.rad * self.factor
            else:
                radius = self.rad
            xc = self.xpos + math.cos(theta*i-theta/2) * radius
            yc = self.ypos + math.sin(theta*i-theta/2) * radius
            pts_star.append(rg.Point3d(xc,yc,0.2))
        
        curve_star = rg.NurbsCurve.Create(True,1,pts_star)
        star = rg.Brep.CreatePlanarBreps(curve_star,0.001)
        return star

# Initial variables
flagLength = 2880 #mm
flagWidth = 1920 #mm

# Draw stars
star1 = Star(Patterns[0].X,Patterns[0].Y,200,5,0.4)
star2 = Star(Patterns[1].X,Patterns[1].Y,70,5,0.4)
star3 = Star(Patterns[2].X,Patterns[2].Y,70,5,0.4)
star4 = Star(Patterns[3].X,Patterns[3].Y,70,5,0.4)
star5 = Star(Patterns[4].X,Patterns[4].Y,70,5,0.4)
Stars = []
Stars=star1.draw()
Stars += star2.draw()
Stars+= star2.draw()
Stars+=star3.draw()
Stars+=star4.draw()
Stars+=star5.draw()

# Draw background
RectangleSurface = rg.NurbsSurface.CreateFromCorners(rg.Point3d(0,0,0), rg.Point3d(flagLength,0,0), rg.Point3d(flagLength, flagWidth, 0), rg.Point3d(0,flagWidth,0))