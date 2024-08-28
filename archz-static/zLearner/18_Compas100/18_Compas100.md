# Compas 100%

---

- [**After noticing the power of compass, I am planning to use compass library for everything: geometry, algorithm, robotic control, etc. The ideal platform is Linux/ubuntu. I am imaging that I can be independent from other software/library for coding like RhinoGeometry, Grasshopper, etc.**](#after-noticing-the-power-of-compass-i-am-planning-to-use-compass-library-for-everything-geometry-algorithm-robotic-control-etc-the-ideal-platform-is-linuxubuntu-i-am-imaging-that-i-can-be-independent-from-other-softwarelibrary-for-coding-like-rhinogeometry-grasshopper-etc)
- [Compas lecture 01](#compas-lecture-01)
- [Compas lecture 02](#compas-lecture-02)
- [Compas lecture 03](#compas-lecture-03)
- [Compas lecture 04](#compas-lecture-04)
- [COMPAS lecture 05](#compas-lecture-05)
- [COMPAS lecture 06](#compas-lecture-06)
- [COMPAS lecture 07](#compas-lecture-07)


---
**After noticing the power of compass, I am planning to use compass library for everything: geometry, algorithm, robotic control, etc. The ideal platform is Linux/ubuntu. I am imaging that I can be independent from other software/library for coding like RhinoGeometry, Grasshopper, etc.**
--

## Compas lecture 01
 - Gain the ability to design, plan and execute robotic fabrication processes using python

![](18_Compas100/18_Compas100_2023-02-20-16-42-56.png)
![](18_Compas100/18_Compas100_2023-02-20-16-33-46.png)
![](18_Compas100/18_Compas100_2023-02-20-16-34-08.png)
![](18_Compas100/18_Compas100_2023-02-20-16-34-41.png)
![](18_Compas100/18_Compas100_2023-02-20-16-34-50.png)
![](18_Compas100/18_Compas100_2023-02-20-16-34-56.png)
![](18_Compas100/18_Compas100_2023-02-20-16-35-03.png)

## Compas lecture 02
![](18_Compas100/18_Compas100_2023-02-27-15-57-36.png)
![](18_Compas100/18_Compas100_2023-02-27-15-58-23.png)
![](18_Compas100/18_Compas100_2023-02-27-16-00-38.png)
![](18_Compas100/18_Compas100_2023-02-27-16-03-31.png)
![](18_Compas100/18_Compas100_2023-02-27-16-04-45.png)
![](18_Compas100/18_Compas100_2023-02-27-16-10-10.png)

 - Example:
 ```python
      """There are several ways to construct a `Frame`.
      """
      from compas.geometry import Point
      from compas.geometry import Vector
      from compas.geometry import Frame
      from compas.geometry import Plane

      # Frame autocorrects axes to be orthonormal
      F = Frame(Point(1, 0, 0), Vector(-0.45, 0.1, 0.3), Vector(1, 0, 0))

      F = Frame([1, 0, 0], [-0.45, 0.1, 0.3], [1, 0, 0])

      F = Frame.from_points([1, 1, 1], [2, 3, 6], [6, 3, 0])
      F = Frame.from_plane(Plane([0, 0, 0], [0.5, 0.2, 0.1]))
      F = Frame.from_euler_angles([0.5, 1.0, 0.2])
      F = Frame.worldXY()
 ```
![](18_Compas100/18_Compas100_2023-02-27-16-30-44.png)
![](18_Compas100/18_Compas100_2023-02-27-16-34-19.png)
![](18_Compas100/18_Compas100_2023-02-27-16-34-55.png)
![](18_Compas100/18_Compas100_2023-02-27-16-35-50.png)
![](18_Compas100/18_Compas100_2023-02-27-16-37-10.png)
![](18_Compas100/18_Compas100_2023-02-27-16-38-10.png)
![](18_Compas100/18_Compas100_2023-02-27-16-38-16.png)
![](18_Compas100/18_Compas100_2023-02-27-16-50-31.png)
![](18_Compas100/18_Compas100_2023-02-27-16-55-14.png)
![](18_Compas100/18_Compas100_2023-02-27-16-56-33.png)
![](18_Compas100/18_Compas100_2023-02-27-16-56-39.png)
![](18_Compas100/18_Compas100_2023-02-27-16-56-45.png)
![](18_Compas100/18_Compas100_2023-02-27-16-56-58.png)
![](18_Compas100/18_Compas100_2023-02-27-16-57-26.png)
![](18_Compas100/18_Compas100_2023-02-27-16-57-39.png)
![](18_Compas100/18_Compas100_2023-02-27-16-57-46.png)

## Compas lecture 03
![](18_Compas100/18_Compas100_2023-03-06-16-02-21.png)
![](18_Compas100/18_Compas100_2023-03-06-16-03-43.png)
![](18_Compas100/18_Compas100_2023-03-06-16-18-28.png)
![](18_Compas100/18_Compas100_2023-03-06-16-19-43.png)
![](18_Compas100/18_Compas100_2023-03-06-16-19-49.png)
![](18_Compas100/18_Compas100_2023-03-06-16-20-08.png)
![](18_Compas100/18_Compas100_2023-03-06-16-20-16.png)
![](18_Compas100/18_Compas100_2023-03-06-16-20-21.png)
![](18_Compas100/18_Compas100_2023-03-06-16-20-28.png)
![](18_Compas100/18_Compas100_2023-03-06-16-20-34.png)
![](18_Compas100/18_Compas100_2023-03-06-16-28-14.png)
![](18_Compas100/18_Compas100_2023-03-06-16-55-47.png)
![](18_Compas100/18_Compas100_2023-03-06-16-55-52.png)
![](18_Compas100/18_Compas100_2023-03-06-16-55-58.png)
![](18_Compas100/18_Compas100_2023-03-06-16-56-03.png)
![](18_Compas100/18_Compas100_2023-03-06-16-56-11.png)
![](18_Compas100/18_Compas100_2023-03-06-16-56-22.png)
![](18_Compas100/18_Compas100_2023-03-06-16-56-26.png)
![](18_Compas100/18_Compas100_2023-03-06-16-56-30.png)
![](18_Compas100/18_Compas100_2023-03-06-16-56-38.png)


## Compas lecture 04
![](18_Compas100/18_Compas100_2023-03-19-16-32-54.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-03.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-09.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-16.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-21.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-26.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-31.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-37.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-43.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-48.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-52.png)
![](18_Compas100/18_Compas100_2023-03-19-16-33-57.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-01.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-06.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-10.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-15.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-19.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-25.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-29.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-33.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-38.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-42.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-46.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-51.png)
![](18_Compas100/18_Compas100_2023-03-19-16-34-56.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-02.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-07.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-11.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-15.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-23.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-30.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-34.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-39.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-43.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-47.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-51.png)
![](18_Compas100/18_Compas100_2023-03-19-16-35-58.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-02.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-06.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-10.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-14.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-18.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-23.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-29.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-33.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-38.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-43.png)
![](18_Compas100/18_Compas100_2023-03-19-16-36-49.png)

## COMPAS lecture 05

![](18_Compas100/18_Compas100_2023-03-26-14-26-52.png)
![](18_Compas100/18_Compas100_2023-03-26-14-29-24.png)
![](18_Compas100/18_Compas100_2023-03-26-14-30-44.png)
![](18_Compas100/18_Compas100_2023-03-26-14-31-04.png)
![](18_Compas100/18_Compas100_2023-03-26-14-32-36.png)
![](18_Compas100/18_Compas100_2023-03-26-14-33-47.png)
![](18_Compas100/18_Compas100_2023-03-26-14-57-35.png)
![](18_Compas100/18_Compas100_2023-03-26-15-04-19.png)
![](18_Compas100/18_Compas100_2023-03-26-15-04-24.png)
![](18_Compas100/18_Compas100_2023-03-26-15-04-29.png)

![](18_Compas100/18_Compas100_2023-03-26-15-08-00.png)
![](18_Compas100/18_Compas100_2023-03-26-15-08-03.png)
![](18_Compas100/18_Compas100_2023-03-26-15-08-07.png)
![](18_Compas100/18_Compas100_2023-03-26-15-08-12.png)
![](18_Compas100/18_Compas100_2023-03-26-15-08-16.png)
![](18_Compas100/18_Compas100_2023-03-26-15-08-21.png)
![](18_Compas100/18_Compas100_2023-03-26-15-08-25.png)

## COMPAS lecture 06
![](18_Compas100/18_Compas100_2023-04-03-15-54-35.png)
![](18_Compas100/18_Compas100_2023-04-03-15-54-56.png)
![](18_Compas100/18_Compas100_2023-04-03-15-59-47.png)

![](18_Compas100/18_Compas100_2023-04-03-16-16-17.png)
![](18_Compas100/18_Compas100_2023-04-03-16-16-24.png)
![](18_Compas100/18_Compas100_2023-04-03-16-18-46.png)
![](18_Compas100/18_Compas100_2023-04-03-16-19-33.png)
![](18_Compas100/18_Compas100_2023-04-03-16-20-01.png)
![](18_Compas100/18_Compas100_2023-04-03-16-22-49.png)

![](18_Compas100/18_Compas100_2023-04-03-16-29-18.png)
![](18_Compas100/18_Compas100_2023-04-03-16-31-40.png)


## COMPAS lecture 07

![](18_Compas100/COMPAS_页面_05.png)
![](18_Compas100/COMPAS_页面_06.png)
![](18_Compas100/COMPAS_页面_07.png)
![](18_Compas100/COMPAS_页面_08.png)
![](18_Compas100/COMPAS_页面_09.png)
![](18_Compas100/COMPAS_页面_10.png)
![](18_Compas100/COMPAS_页面_11.png)
![](18_Compas100/COMPAS_页面_12.png)
![](18_Compas100/COMPAS_页面_13.png)
![](18_Compas100/COMPAS_页面_14.png)
![](18_Compas100/COMPAS_页面_15.png)
![](18_Compas100/COMPAS_页面_16.png)
![](18_Compas100/COMPAS_页面_17.png)
![](18_Compas100/COMPAS_页面_18.png)
![](18_Compas100/COMPAS_页面_19.png)
![](18_Compas100/COMPAS_页面_20.png)
![](18_Compas100/COMPAS_页面_21.png)
![](18_Compas100/COMPAS_页面_22.png)
![](18_Compas100/COMPAS_页面_23.png)
![](18_Compas100/COMPAS_页面_24.png)
![](18_Compas100/COMPAS_页面_25.png)
![](18_Compas100/COMPAS_页面_26.png)
![](18_Compas100/COMPAS_页面_27.png)
![](18_Compas100/COMPAS_页面_28.png)
![](18_Compas100/COMPAS_页面_29.png)
![](18_Compas100/COMPAS_页面_30.png)
![](18_Compas100/COMPAS_页面_31.png)
![](18_Compas100/COMPAS_页面_32.png)
![](18_Compas100/COMPAS_页面_33.png)
![](18_Compas100/COMPAS_页面_34.png)




