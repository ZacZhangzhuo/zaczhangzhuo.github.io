# Grasshopper-Python 贪吃蛇


![](\images\0001.jpg)

代码如下：

```Python
     import scriptcontext as sc
    import rhinoscriptsyntax as rs
    import random
    import Rhino.Geometry as rg
    import copy
    import math

    def UnitizePoint(point):
        point = rg.Vector3d(point.X,point.Y,0)
        rg.Vector3d.Unitize(point)
        point = rg.Point3d(point.X,point.Y,0)
        return point

    def DirectionalMove (Direction):
        DirectionVec = rg.Vector3d(Direction.X-0.5, Direction.Y-0.5,0)
        rg.Vector3d.Unitize(DirectionVec)
        VecX = rg.Vector3d.XAxis

        if DirectionVec.Y >= 0:
        if DirectionVec*VecX > math.cos(math.pi/8):
            DirectionVec = rg.Vector3d(1,0,0)
        elif  DirectionVec*VecX <= math.cos(math.pi/8) and DirectionVec*VecX > math.cos(math.pi*3/8):
            DirectionVec = rg.Vector3d(1,1,0)
        elif  DirectionVec*VecX <= math.cos(math.pi*3/8) and DirectionVec*VecX > math.cos(math.pi*5/8):
            DirectionVec = rg.Vector3d(0,1,0)
        elif  DirectionVec*VecX <= math.cos(math.pi*5/8) and DirectionVec*VecX > math.cos(math.pi*7/8):
            DirectionVec = rg.Vector3d(-1,1,0)
        elif  DirectionVec*VecX <= math.cos(math.pi*7/8):
            DirectionVec = rg.Vector3d(-1,0,0)
        else:
        if DirectionVec*VecX > math.cos(math.pi/8):
            DirectionVec = rg.Vector3d(1,0,0)
        elif  DirectionVec*VecX <= math.cos(math.pi/8) and DirectionVec*VecX > math.cos(math.pi*3/8):
            DirectionVec = rg.Vector3d(1,-1,0)
        elif  DirectionVec*VecX <= math.cos(math.pi*3/8) and DirectionVec*VecX > math.cos(math.pi*5/8):
            DirectionVec = rg.Vector3d(0,-1,0)
        elif  DirectionVec*VecX <= math.cos(math.pi*5/8) and DirectionVec*VecX > math.cos(math.pi*7/8):
            DirectionVec = rg.Vector3d(-1,-1,0)
        elif  DirectionVec*VecX <= math.cos(math.pi*7/8):
            DirectionVec = rg.Vector3d(-1,0,0)

        rg.Vector3d.Unitize(DirectionVec)
        return DirectionVec

    scale = 0.03
    tailLength = 20
    dotRange = 50
    Direction = DirectionalMove(Direction)
    snakeCircles = []
    tailCircles = []
    dots = []

    # Add the variables to the sticky dict
    if "snakeLocations" not in sc.sticky:
        sc.sticky["snakeLocations"] = []
        sc.sticky["snakeLocations"].append(rg.Point3d(0,0,0))

    if "foodLocation" not in sc.sticky:
        sc.sticky["foodLocation"] = rg.Point3d(0,0,0)
        
    if "score" not in sc.sticky:
        sc.sticky["score"] = 0
        
    if "Tails" not in sc.sticky:
        sc.sticky["Tails"] = []
        
    #Die
    if sc.sticky["snakeLocations"][0].X > FoodRange or sc.sticky["snakeLocations"][0].X < -FoodRange or sc.sticky["snakeLocations"][0].Y > FoodRange or sc.sticky["snakeLocations"][0].Y < -FoodRange:
        Run = False

    # Run
    if Reset:
        sc.sticky["score"] = 0
        sc.sticky["snakeLocations"] = []
        sc.sticky["Tails"] = []
        sc.sticky["snakeLocations"].append(rg.Point3d(0,0,0))
        random.seed(1)
        sc.sticky["foodLocation"] = rg.Point3d(random.uniform(-FoodRange,FoodRange),random.uniform(-FoodRange,FoodRange),0)
        
    elif not Run:
        print 'NOT Runing'
        
    else:
        #With trigger
        if len(sc.sticky["snakeLocations"]) <= 1:
            sc.sticky["snakeLocations"][0].X += Direction.X
            sc.sticky["snakeLocations"][0].Y += Direction.Y
        else:
            tempSnake = copy.deepcopy(sc.sticky["snakeLocations"])
            for i in range(len(sc.sticky["snakeLocations"])):
                sc.sticky["snakeLocations"][i].X = tempSnake[i-1].X
                sc.sticky["snakeLocations"][i].Y = tempSnake[i-1].Y

            sc.sticky["Tails"].append(copy.deepcopy(sc.sticky["snakeLocations"][0]))
            if len(sc.sticky["Tails"]) >= tailLength:
                sc.sticky["Tails"].pop(0)

            sc.sticky["snakeLocations"][0].X = sc.sticky["snakeLocations"][1].X+Direction.X
            sc.sticky["snakeLocations"][0].Y = sc.sticky["snakeLocations"][1].Y+Direction.Y

        if rg.Point3d.DistanceTo(sc.sticky["snakeLocations"][0], sc.sticky["foodLocation"]) < scale*FoodRange :
            sc.sticky["score"] += 1
            sc.sticky["snakeLocations"].append(rg.Point3d(sc.sticky["snakeLocations"][-1].X-Direction.X,sc.sticky["snakeLocations"][-1].Y-Direction.Y,0))
            sc.sticky["foodLocation"] = rg.Point3d(random.uniform(-FoodRange,FoodRange),random.uniform(-FoodRange,FoodRange),0)

    # Return value
    for snakeLocations in sc.sticky["snakeLocations"]:
        snakeCircles.append(rg.Circle(rg.Plane(snakeLocations,rg.Vector3d.ZAxis), 1))
    Score = 'Score: ' + str(sc.sticky["score"])

    Snake = snakeCircles
    Foods = rg.Circle(rg.Plane(sc.sticky["foodLocation"],rg.Vector3d.ZAxis), scale*FoodRange)
    Bound = rg.Rectangle3d(rg.Plane(rg.Point3d(-FoodRange,-FoodRange,0),rg.Vector3d.ZAxis),2*FoodRange,2*FoodRange)

    for Tails in sc.sticky["Tails"]:
        tailCircles.append(rg.Circle(rg.Plane(Tails,rg.Vector3d.ZAxis), 1))
    Tails = tailCircles

    for i in range(dotRange):
        for j in range(dotRange):
            dots.append(rg.Point3d(FoodRange/dotRange+i*(2*FoodRange/dotRange)-FoodRange, FoodRange/dotRange+j*(2*FoodRange/dotRange)-FoodRange, 0))
            
    Dots = dots
```
---

希望能给你带来点启发。

---
