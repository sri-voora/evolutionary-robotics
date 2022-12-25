import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.world=WORLD()
        self.robot=ROBOT()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            #backLegTargetAngles.append(c.backLegAmplitude*numpy.sin(c.backLegFrequency*(i*c.step)+c.backLegPhaseOffSet))
            #frontLegTargetAngles.append(c.frontLegAmplitude*numpy.sin(c.frontLegFrequency*(i*c.step)+c.frontLegPhaseOffSet))
            #pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_BackLeg', controlMode=p.POSITION_CONTROL, targetPosition=(backLegTargetAngles[i]), maxForce=30)
            #pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_FrontLeg', controlMode=p.POSITION_CONTROL, targetPosition=(frontLegTargetAngles[i]), maxForce=30)
            time.sleep(1/60)
            self.robot.Sense(i)
            #print(i)

    def __del__(self):
        p.disconnect()