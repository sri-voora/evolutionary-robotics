import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        #self.motors={}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        self.PrepareToSense()

    def PrepareToSense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName]=SENSOR(linkName)
    
    def Sense(self,t):
        #backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        for sens in self.sensors:
            self.sensors[sens].Get_Value(t)
            print(self.sensors[sens])