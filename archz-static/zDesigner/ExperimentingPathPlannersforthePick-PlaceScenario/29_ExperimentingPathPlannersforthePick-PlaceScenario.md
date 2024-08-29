# Experimenting Path Planners for the Pick-Place Scenario

---

It is a part of the COMPAS II assignment. Some trails to extend for exploring the path planning algorithms as personal interest and for the future work of the project.

---

<iframe id="iframe" src="https://www.youtube.com/embed/bxeMlPWHJbk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---




## Calculating the trajectories
```python

    """
    Calculate pickup of a part.
    """

    from compas.geometry import Frame
    from compas_fab.robots import PlanningScene
    from compas.robots import Configuration
    import math
    import os
    from copy import deepcopy
    from compas import json_dump,json_load
    from compas_fab.backends import RosClient
    from compas_fab.robots import Tool

    def reverse_trajectory(trajectory):
        out_trajectory = deepcopy(trajectory)
        out_trajectory.points = list(reversed(trajectory.points))
        return out_trajectory



    with RosClient("localhost") as client:
        robot = client.load_robot()
        scene = PlanningScene(robot)
        tolerance_above = 0.001
        tolerance_below = 0.001
        all_trajectories = []

        

        data = json_load('data.json')
        group, c_visual_mesh, tcf_frame, assembly, pick_frame, approach_distance, planner_id = data['group'], data['c_visual_mesh'], data['tcf_frame'], data['assembly'], data['pick_frame'], data['approach_distance'], data['planner_id']
        tool = Tool(c_visual_mesh, tcf_frame, c_visual_mesh)
        robot.attach_tool(tool, group)
        """
        Pick trajectory
        """
        approach_pick_frame = Frame(pick_frame.point +(pick_frame.normal*approach_distance), pick_frame.xaxis, pick_frame.yaxis)

        start_configuration = Configuration.from_revolute_values([0,0,0,0,math.pi/2,0])
        approach_pick_config = robot.inverse_kinematics(approach_pick_frame, start_configuration, group)
        pick_config = robot.inverse_kinematics(pick_frame, approach_pick_config, group)

        # !
        goal_constraints = robot.constraints_from_configuration(configuration=pick_config, tolerances_above=[tolerance_above], tolerances_below=[tolerance_below], group=group)
        pick_trajectory = robot.plan_motion(
            goal_constraints,
            start_configuration=approach_pick_config,
            group=group,
            options=dict(
                planner_id=planner_id,
            ),
        )

        print ('start planning with ' + planner_id+'...')
        for i in range(assembly.attributes['count']):
        # for i in range(0,18):
            print ('Planning part %d successfully' % i)

            """
            Place
            """
            part = assembly.find_by_key(i)
            place_frame = part.attributes['place_frame']
            approach_place_frame = Frame(place_frame.point + [0, 0, approach_distance], place_frame.xaxis, place_frame.yaxis)

            approach_place_config = robot.inverse_kinematics(approach_place_frame, start_configuration, group)
            place_config = robot.inverse_kinematics(place_frame, approach_place_config, group)

            # !
            goal_constraints = robot.constraints_from_configuration(configuration=place_config, tolerances_above=[tolerance_above], tolerances_below=[tolerance_below], group=group)
            place_trajectory = robot.plan_motion(
                goal_constraints,
                start_configuration=approach_place_config,
                group=group,
                options=dict(
                    planner_id=planner_id,
                ),
            )

            ''' 
            Pick to place
            '''
            goal_constraints = robot.constraints_from_configuration(configuration=approach_place_config, tolerances_above=[tolerance_above], tolerances_below=[tolerance_below], group=group)
            pick_to_place_trajectory = robot.plan_motion(
                goal_constraints,
                start_configuration=approach_pick_config,
                group=group,
                options=dict(
                    planner_id=planner_id,
                ),
            )

            all_trajectories.extend( [pick_trajectory, reverse_trajectory(pick_trajectory), pick_to_place_trajectory, place_trajectory, reverse_trajectory(place_trajectory),reverse_trajectory(pick_to_place_trajectory)])
            # all_trajectories.extend( [ place_config])


    json_dump(all_trajectories, 'trajectories.json', True)
    print ('Trajectories saved successfully in trajectories.json')


```

---

## Sending the trajectories to the robot

```python
    import compas_rrc as rrc
    from compas_fab.robots import to_degrees
    from compas import json_load
    from compas_fab.backends import RosClient
    from compas_fab.robots import PlanningScene
    from compas_fab.robots import Tool


    io_signal = 'doUnitC141Out16'
    speed = 200


    def send_trajectory(abb, robot, speed, points, last_point_fine=True):
        for i in range(len(points)):
            c = points[i]
            joints = to_degrees(c.joint_values)
            if i < len(points) - 1:
                zone = rrc.Zone.Z10
            else:
                zone = rrc.Zone.FINE if last_point_fine else rrc.Zone.Z10

            abb.send(rrc.MoveToJoints(joints, ext_axes=[], speed=speed, zone=zone))


    with RosClient("localhost") as client:
        robot = client.load_robot()
        scene = PlanningScene(robot)

        data = json_load('data.json')
        group, c_visual_mesh, tcf_frame, assembly, pick_frame, approach_distance, planner_id = data['group'], data['c_visual_mesh'], data['tcf_frame'], data['assembly'], data['pick_frame'], data['approach_distance'], data['planner_id']
        tool = Tool(c_visual_mesh, tcf_frame, c_visual_mesh)
        robot.attach_tool(tool, group)

        abb = rrc.AbbClient(client)
        trajectories = json_load('trajectories.json')

        abb.send(rrc.PrintText("Sending {} PnP points. Press play to move".format(len(trajectories))))
        abb.send(rrc.Stop())

        for i in range(int(len(trajectories)/6)):
            send_trajectory(abb, robot, speed, trajectories[6*i].points)
            # abb.send(rrc.SetDigital(io_signal, 1))
            abb.send(rrc.WaitTime(1))
            send_trajectory(abb, robot, speed, trajectories[6*i+1].points, last_point_fine=False)
            send_trajectory(abb, robot, speed, trajectories[6*i+2].points, last_point_fine=False)
            send_trajectory(abb, robot, speed,trajectories[6*i+3].points)
            # abb.send(rrc.SetDigital(io_signal, 0))
            abb.send(rrc.WaitTime(1))
            send_trajectory(abb, robot, speed, trajectories[6*i+4].points, last_point_fine=False)
            send_trajectory(abb, robot, speed, trajectories[6*i+5].points)

```