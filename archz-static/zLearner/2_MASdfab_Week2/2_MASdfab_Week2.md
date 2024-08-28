# MAS dfab - Week 2 - Computational Art

---

Contents
- [Enumeration](#enumeration)
- [Interval](#interval)
- [Read images](#read-images)
- [Remap function](#remap-function)
- [Ask the colour of the pixie](#ask-the-colour-of-the-pixie)
- [Mesh Colour (Colour is stored in the vertex data)](#mesh-colour-colour-is-stored-in-the-vertex-data)
- [One reason why AutoCompletion does not work on my PC](#one-reason-why-autocompletion-does-not-work-on-my-pc)

##  Enumeration

```Python
    for i, rectangle in enumerate(geo): #!
        r = deepcopy(rectangle)
        degree = math.radians(random.randint(-rectangle, Corner(2).Y))

        # The for loop is the same as below

    for i in range(len(geo)):  #!
        r = deepcopy(rectangle)
        degree = math.radians(random.randint(-rectangle, Corner(2).Y))
```

##  Interval

- Represents an interval in one-dimensional space, that is defined as two extrema or bounds.
- https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Interval.htm

##  Read images

```Python
    import System
    import os

    HERE = ghenv.LocalScope.ghdoc.Path
    dir_path = os.path.dirname(HERE)
    bitmap = System.Drawing.Image.FromFile(dir_path + "\\" + inTemp + ".png")

    deltaPixelX = bitmap.Width / nx
    deltaPixelT = bitmap.Height / ny

    # Ask the colour of the pixie
    color = System.Drawing.Bitmap.GetPixel(bitmap, x, y)
```

##  Remap function

```Python
    def remap(value, low1, high1, low2, high2):
        new_value = low2 + (value-low1)*(high2-low2)/(high1-low1)
        return new_value
```

##  Ask the colour of the pixie

```Python
    import System
    import os

    HERE = ghenv.LocalScope.ghdoc.Path
    dir_path = os.path.dirname(HERE)
    bitmap = System.Drawing.Image.FromFile(dir_path + "\\" + inTemp + ".png")

    deltaPixelX = bitmap.Width / nx
    deltaPixelT = bitmap.Height / ny

    # Ask the colour of the pixie
    color = System.Drawing.Bitmap.GetPixel(bitmap, x, y)
```

##  Mesh Colour (Colour is stored in the vertex data)

```Python
    box_mesh.VertexColors.CreateMonotoneMesh(self.color)
```

## One reason why AutoCompletion does not work on my PC

* Some other paths occupied the AutoCompletion but cannot do that well. So we have to clear every extra path, and don't let the useless things exist.

```Json
      "python.autoComplete.extraPaths": [
  
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\scripts",
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
    "C:\\Applications\\Rhino 7\\Plug-ins\\IronPython\\Lib",
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
    // There is a "C:\Program Files\Common Files\McNeel\Rhinoceros\7.0\Plug-ins\CodeListener" very annoying and occupied the autoCompletion when scripting GHPython. Delete this one then autoCompletion is fine.
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib\\ghpythonlib"
  ],
```