import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

class SENSOR:
    def __init__(self, linkName):
        self.linkName=linkName
        
        self.Prepare_To_Sense()
    
    def Prepare_To_Sense(self):
        self.sensorValues=numpy.zeros(1000)
    
    def Get_Value(self, i):
        self.sensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #if i==999:
            #print(self.sensorValues)
            #pass
    
    def Save_Values(self):
        numpy.save("data/sensorValues.npy", self.sensorValues)