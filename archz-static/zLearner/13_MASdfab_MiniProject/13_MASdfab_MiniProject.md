# MAS dfab - Mini Project



## New orientation function

```Python
def OrientPlane(plane):
    zAxis = plane.ZAxis
    if zAxis.Z < 0: zAxis = -zAxis
    outPlane = rg.Plane(plane.Origin, zAxis)
    xAxis = copy.copy(outPlane.XAxis)
    xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, outPlane.YAxis))
    outPlane.Transform(rg.Transform.Rotation(outPlane.XAxis, xAxis, outPlane.Origin))
    if outPlane.YAxis.Z <0 : outPlane = rg.Plane(outPlane.Origin, -outPlane.XAxis, -outPlane.YAxis)
    return outPlane
```

## An interesting Q&A

![](13_MASdfab_MiniProject/13_MASdfab_MiniProject_2022-12-07-09-54-22.png)


## gitignore
- bin/: 忽略当前路径下的bin文件夹，该文件夹下的所有内容都会被忽略，不忽略 bin 文件
- /bin: 忽略根目录下的bin文件
- /*.c: 忽略 cat.c，不忽略 build/cat.c
- debug/*.obj: 忽略 debug/io.obj，不忽略 debug/common/io.obj 和 tools/debug/io.obj
- **/foo: 忽略/foo, a/foo, a/b/foo等
- a/**/b: 忽略a/b, a/x/b, a/x/y/b等
- !/bin/run.sh: 不忽略 bin 目录下的 run.sh 文件
- *.log: 忽略所有 .log 文件
- config.php: 忽略当前路径的 config.php 文件
