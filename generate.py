import numpy as np

import pyrosim.pyrosim as ps



def Create_World():
    ps.Start_SDF("box.sdf")
    l = 1
    w = 1
    h = 1
    x = 0
    y = 0
    z = 0.5
    for i in range(10):
        ps.Send_Cube(name="Box", pos=[x,y,z],size=[l,w,h])
        z += h
        l = 0.9 * l
        w = 0.9 * w
        h = 0.9 * h

    ps.End()

def Create_Robot():

    ps.Start_URDF("body.urdf")
    l = 0.2
    w = 0.2
    h = 0.2
    x = 0
    y = 0
    z = 0.5
    # ps.Send_Cube(name="Foot",pos=[x,y,z], size=[l,w,h]) #Parent
    # ps.Send_Joint(name="Foot_Torso", parent="Foot", child="Torso", type="revolute", position = [0.5,0,1.0])
    # ps.Send_Cube(name="Torso",pos=[0.5,0,0.5],size=[l,w,h]) #Child
    # ps.Send_Joint(name="Foot2_Torso", parent="Torso", child="Foot2", type="revolute", position = [1.0,0,1.0])
    # ps.Send_Cube(name="Foot2",pos=[0.5,0,0.5], size=[l,w,h])
    # ps.Send_Joint(name="Foot3_Foot2", parent="Foot2", child="Foot3", type="revolute", position= [1.0, 0, 1.0])
    # ps.Send_Cube(name="Foot3", pos=[0.5,0,0.5], size=[l*3,w*3,h*3])
    ps.Send_Cube(name="Body", pos=[0, 0, 0.9], size=[0.5, 0.5, 0.5])
    ps.Send_Cube(name="Chain1", pos=[0, 0, 0.65],
                 size=[l, w, h])  # Adjusted to be 0.25 (half of Body) + 0.1 (half of Chain1)
    ps.Send_Cube(name="Chain2", pos=[0, 0, 0.45], size=[l, w, h])  # Adjusted similarly for Chain2
    ps.Send_Cube(name="Chain3", pos=[0, 0, 0.25], size=[l, w, h])  # Adjusted for Chain3
    ps.Send_Cube(name="Chain4", pos=[0, 0, 0.05], size=[l, w, h])  # Adjusted for Chain4
      # Create 4 links
    ps.Send_Joint(name="Body_Chain1", parent="Body", child="Chain1", type='revolute', position=[0, 0, 0.65])
    ps.Send_Joint(name="Chain1_Chain2", parent="Chain1", child="Chain2", type='revolute', position=[0, 0, 0.45])
    ps.Send_Joint(name="Chain2_Chain3", parent="Chain2", child="Chain3", type='revolute', position=[0, 0, 0.25])
    ps.Send_Joint(name="Chain3_Chain4", parent="Chain3", child="Chain4", type='revolute', position=[0, 0, 0.05])
    # # Connecting the body to the first chain link
    # ps.Send_Joint(name="Body_First", parent="Body", child=chain_links[0], type='revolute', position=[0, 0, 0.4])
    #
    # # Connecting the rest of the chain links
    # for i in range(len(chain_links) - 1):
    #     ps.Send_Joint(name="Chain", parent=chain_links[i], child=chain_links[i + 1], type='revolute',position=[0, 0, 0.5 - (i + 1) * 0.2])

    ps.End()

Create_Robot()