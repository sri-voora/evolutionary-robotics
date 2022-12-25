import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName=jointName
        
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude=c.amplitude
        self.frequency=c.frequency
        self.offSet=c.phaseOffSet
        
        if self.jointName==b'Torso_BackLeg':
            self.frequency=self.frequency/2
            pass

        self.motorValues=self.amplitude*numpy.sin(self.frequency*(numpy.linspace(0,(2*numpy.pi),1000))+self.offSet)

    def Set_Value(self, robotId, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=self.motorValues[t], maxForce=30)
    
    def Save_Values(self):
        numpy.save("data/motorValues.npy", self.motorValues)