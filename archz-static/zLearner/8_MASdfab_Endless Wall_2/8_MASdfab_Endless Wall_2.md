# MAS dfab - Endless Wall - 2


- [Infinite looping](#infinite-looping)
- [Listen to the robot](#listen-to-the-robot)
- [Robot position judgement](#robot-position-judgement)
- [Sending codes to the robot](#sending-codes-to-the-robot)
- [Simple command scripts](#simple-command-scripts)

## Infinite looping

```Python
import math


def getZ(Plane):
    return Plane.Origin.Z


Count = 10
Tolerance = 0.01

RemovePlanes = []
TargetPlanes = []
for count in range(Count):

    # for i in range(
    listLength = 100000000
    for i in range(10):
        length = len(list(data.Branch(i)))
        if length < listLength:
            listLength = length

    initPlanes = list(data.Branch((count) % Count))[:listLength]
    theTargetPlanes = list(data.Branch((count + 1) % Count))[:listLength]

    iterations = 0

    keepPlanes = []
    theRemovePlanes = []
    for n, p in enumerate(initPlanes):
        temp = True
        for m, i in enumerate(theTargetPlanes):
            iterations += 1
            if p.Origin.DistanceTo(i.Origin) < Tolerance:
                # initPlanes.pop(n)
                theTargetPlanes.pop(m)
                temp = False
                keepPlanes.append(p)
                break
        if temp == True:
            theRemovePlanes.append(p)

    theRemovePlanes.sort(key=getZ, reverse=True)
    theTargetPlanes.sort(key=getZ, reverse=False)

    RemovePlanes.extend(theRemovePlanes)
    TargetPlanes.extend(theTargetPlanes)

```

## Listen to the robot
```Python
import simple_comm as comm

if listen:
    chunks = comm.listen_to_robot("192.168.10.10")
    config = chunks["actual_joints"]
```

## Robot position judgement
```Python
import math
import scriptcontext as rs

fabricate = run

if x: rs.sticky["count"] -=1
if reset:
    rs.sticky["count"] = 0

temp = 0
for i in range(len(current_configuration)):
    if round(current_configuration[i], 1) == round(stop_configuration[i], 1):
        temp += 1

if temp == 6:
    rs.sticky["count"] += 1
    fabricate = True

count = rs.sticky["count"]

```

## Sending codes to the robot
```Python
from imp import reload
import Rhino.Geometry as rg
import simple_ur_script as ur
# reload(ur)
import simple_comm as c
# reload(c)

def tcp(script):
    script += ur.set_tcp_by_angles(TCP[0], TCP[1], TCP[2], TCP[3], TCP[4], TCP[5])
    return script


def set_robot_base():
    pt_0 = TABLE_NAVIGATION_POINTS[0]  # base plane origin
    pt_1 = TABLE_NAVIGATION_POINTS[1]
    pt_2 = TABLE_NAVIGATION_POINTS[2]
    robot_base = rg.Plane(pt_0, pt_1 - pt_0, pt_2 - pt_0)
    return robot_base


def rhino_to_robot_space(rhino_plane):
    plane = rhino_plane.Clone()
    robot_base_plane = set_robot_base()
    rhino_matrix = rg.Transform.PlaneToPlane(rg.Plane.WorldXY, robot_base_plane)
    plane.Transform(rhino_matrix)
    return plane


def pickup_brick(script, pick_up_plane):
    planes = []
    # change the distance if needed

    safe_plane = pick_up_plane.Clone()
    safe_plane.Translate(rg.Vector3d.ZAxis * SAFE_DIST)

    ## add to the path: go to the safe plane
    script += ur.move_l(safe_plane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(safe_plane)

    ## add to the path: go to the pick up plane
    script += ur.move_l(pick_up_plane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(pick_up_plane)

    ## add to the path: turn on the vacuum and wait 1 sec.
    script += ur.set_digital_out(IO, True)
    script += ur.sleep(SAFE_SLEEP_TIME)

    # add to the path: go back to the safe_plane
    script += ur.move_l(safe_plane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(safe_plane)
    return script, planes

def glue(script, gluePlane):
    planes = []
    safeGluePlane = gluePlane.Clone()
    safeGluePlane.Translate(rg.Vector3d.ZAxis * SAFE_DIST)
    
    script += ur.move_l(safeGluePlane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(safeGluePlane) 
    script += ur.move_l(gluePlane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL) 
    planes.append(gluePlane) 
    script += ur.sleep(SAFE_SLEEP_TIME)
    script += ur.move_l(safeGluePlane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(safeGluePlane) 
    return script, planes


def place_brick(script, place_plane):

    planes = []

    safe_plane = place_plane.Clone()
    safe_plane.Translate(rg.Vector3d.ZAxis * SAFE_DIST)

    # add to the path: go to the safe plane
    script += ur.move_l(safe_plane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(safe_plane)

    # add to the path: go to the place plane
    script += ur.move_l(place_plane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(place_plane)

    ## add to the path: turn off the vacuum and wait 1 second (hold the brick)
    script += ur.set_digital_out(IO, False)
    script += ur.sleep(SAFE_SLEEP_TIME)
    # add to the path: go back to the safe plane
    script += ur.move_l(safe_plane, SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    planes.append(safe_plane)

    return script, planes

test_plane = debug_plane.Clone()
# the_stop_plane = stop_plane.Clone()
# stop_configurations.reverse()

def send(script):
    script = c.concatenate_script(script)
    c.send_script(script, ROBOT_IP)
    return script

if count == None: count = 0

script = ""
script = tcp(script)

if is_debug_mode:
    script += ur.move_l(rhino_to_robot_space(test_plane), SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
    

else:
    if count < len(brick_planes):
        script, p = pickup_brick(
            script, rhino_to_robot_space(picking_planes[count % len(picking_planes)])
        )
        script, p = glue( script, rhino_to_robot_space(gluePlane))
        script, p = place_brick(script, rhino_to_robot_space(brick_planes[count]))
        # script += ur.move_l(rhino_to_robot_space(the_stop_plane), SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
        script += ur.move_j(stop_configurations, SAFE_ROBOT_ACC*5, SAFE_ROBOT_VEL*5)
        
    else:
        if len(continuous_picking_planes) == 0 or len(continuous_brick_planes) ==0:
            pass
        else:
            count = count -  len(brick_planes)

            script, p = pickup_brick(
                script, rhino_to_robot_space(continuous_picking_planes[count % len(continuous_picking_planes)])
            )
            script, p = glue( script, rhino_to_robot_space(gluePlane))
            script, p = place_brick(script, rhino_to_robot_space(continuous_brick_planes[count% len(continuous_brick_planes)]))
            # Zac: add to the path: go to the stop plane
            # script += ur.move_l(rhino_to_robot_space(the_stop_plane), SAFE_ROBOT_ACC, SAFE_ROBOT_VEL)
            script += ur.move_j(stop_configurations, SAFE_ROBOT_ACC*3, SAFE_ROBOT_VEL*3)
            

if fabricate:
    send(script)

```



## Simple command scripts
```Python
import socket
from struct import *
import math
def concatenate_script(list_ur_commands):
    """
    Internal function that concatenates generated UR script into one large script file. Usually used to combine
    scripts generated by the GrasshopperPython components

    Args:
        list_ur_commands: A list of formatted UR Script strings

    Returns:
        ur_script: The concatenated script
    """

    ur_script = "\ndef my_script():\n"
    #ur_script += '\tpopup("running my_script")\n'

    combined_script = ""
    for ur_cmd in list_ur_commands:
        combined_script += ur_cmd

    #format combined script
    lines =  combined_script.split("\n")
    for l in lines:
        ur_script += "\t" + l + "\n"

    ur_script += 'end\n'
    ur_script += '\nmy_script()\n'
    return ur_script

def send_script(script_to_send,robot_ip):
    """
    Opens a socket to the Robot and sends a script

    Args:
        script_to_send: Script to send to socket
        robot_id: Integer. ID of robot

    """

    '''Function that opens a socket connection to the robot'''
    PORT = 30002
    HOST = robot_ip

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((HOST, PORT))
    except:
        print ("Cannot connect to ",HOST,PORT)

    s.settimeout(None)
    max_size= 2<<18
    n=len(script_to_send)
    if n>max_size:
        raise Exception("Program too long")

    try:
        s.send(script_to_send)
    except:
        print("failed to send")
    s.close()

def listen_to_robot(robot_ip):
    PORT = 30003
    HOST = robot_ip
    # Create dictionary to store data
    chunks={}
    chunks["target_joints"] = []
    chunks["actual_joints"]= []
    chunks["forces"] = []
    chunks["pose"] = []
    chunks["time"] = [0]

    data = read(HOST, PORT)
    get_messages(data, chunks)
    return chunks

def read(HOST, PORT):
    """
    Method that opens a TCP socket to the robot, receives data from the robot server and then closes socket

    Returns:
        data: Data broadcast by the robot. In bytes
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((HOST, PORT))
        print "connected"
    except:
        traceback.print_exc()
        print "Cannot connect to ",HOST,PORT
    s.settimeout(None)
    data = s.recv(1024)
    s.close()
    return data

def get_messages(bytes, chunks_info):
    """
    Function parses data stream and selects the following information:
    1) q_target
    2) q_actual
    3) TCP force
    4) Tool Vector
    5) Time

    This data is formatted and the chunks dictionary is updated
    for more info see: http://wiki03.lynero.net/Technical/RealTimeClientInterface
    """


    # get messages
    q_target = bytes[12:60]
    q_actual = bytes[252:300]
    tcp_force = bytes[540:588]
    tool_vector = bytes[588:636]
    controller_time = bytes[740:748]

    # format type: int,
    fmt_double6 = "!dddddd"
    fmt_double1 = "!d"

    #Unpack selected data
    target_joints = unpack(fmt_double6,q_target)
    chunks_info["target_joints"]= (math.degrees(j) for j in target_joints)
    actual_joints = unpack(fmt_double6,q_actual)
    chunks_info["actual_joints"]= (math.degrees(j) for j in actual_joints)
    forces = unpack(fmt_double6,tcp_force)
    chunks_info["forces"]= forces
    pose = unpack(fmt_double6,tool_vector)
    chunks_info["pose"]= pose
    time = unpack(fmt_double1,controller_time)
    chunks_info["time"]= time

```

![](8_MASdfab_Endless%20Wall_2/8_MASdfab_Endless%20Wall_2_2022-11-14-16-54-04.png)
![](8_MASdfab_Endless%20Wall_2/8_MASdfab_Endless%20Wall_2_2022-11-14-16-54-26.png)