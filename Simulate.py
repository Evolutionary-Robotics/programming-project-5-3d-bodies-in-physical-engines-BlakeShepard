import numpy as np

import pyrosim.pyrosim as ps
import pybullet as p
import pybullet_data
import time
from scipy import signal

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
#p.loadSDF("box.sdf")

duration = 10000

ps.Prepare_To_Simulate(robotID)

x = np.linspace(0,10*np.pi, duration)
y = np.sin(x) * 2 * np.pi


forward_increment = 0.01  # Adjust this value for speed
forward_position = 0  # Initialize forward position
for i in range(duration):
    forward_position += forward_increment

    # The target position can still oscillate, but primarily ensure it goes forward
    target_position_body = np.sin(i * 0.1) * 0.4  # Keep oscillation
    force = 100
    ps.Set_Motor_For_Joint(bodyIndex = robotID,
                           jointName = b'Body_Chain1',
                           controlMode = p.POSITION_CONTROL,
                           targetPosition = target_position_body,
                           maxForce = force)
    ps.Set_Motor_For_Joint(bodyIndex=robotID,
                           jointName=b'Chain1_Chain2',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=target_position_body,
                           maxForce=force)
    ps.Set_Motor_For_Joint(bodyIndex=robotID,
                           jointName=b'Chain2_Chain3',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=target_position_body,
                           maxForce=force)
    ps.Set_Motor_For_Joint(bodyIndex=robotID,
                           jointName=b'Chain3_Chain4',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=target_position_body,
                           maxForce=force)
    # ps.Set_Motor_For_Joint(bodyIndex = robotID,
    #                        jointName = b'Foot2_Torso',
    #                        controlMode = p.POSITION_CONTROL,
    #                        targetPosition = y[i],
    #                        maxForce = 100)
    # ps.Set_Motor_For_Joint(bodyIndex = robotID,
    #                        jointName = b'Foot3_Foot2',
    #                        controlMode = p.POSITION_CONTROL,
    #                        targetPosition = y[i],
    #                        maxForce = 100)
    p.stepSimulation()
    time.sleep(1/500)

p.disconnect()